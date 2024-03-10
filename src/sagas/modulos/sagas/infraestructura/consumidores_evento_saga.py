import json
import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from sagas.config import db
from sagas.modulos.sagas.aplicacion.comandos.crear_saga import CrearSaga
from sagas.modulos.sagas.dominio.fabricas import Fabricasagas
from sagas.modulos.sagas.dominio.repositorios import RepositorioSagas
from sagas.modulos.sagas.infraestructura.despachadores import Despachador
from sagas.modulos.sagas.infraestructura.fabricas import FabricaRepositorio
from sagas.modulos.sagas.infraestructura.mapeadores import MapeadorSaga

from sagas.modulos.sagas.infraestructura.schema.v1.eventos import EventoSagaCreado, EventoPropiedadAsociada, EventoInquilinoCreado, EventoPropiedadCreado
from sagas.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearInquilinoPayload, ComandoCrearSaga, ComandoCrearInquilino, ComandoAsociarPropiedadPayload
from sagas.seedwork.aplicacion.comandos import ejecutar_commando
from sagas.seedwork.infraestructura import utils
from sagas.seedwork.infraestructura.uow import UnidadTrabajoPuerto

def suscribirse_a_propiedad_creada(app):
    saga = None
    try:
        saga = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = saga.subscribe('eventos2-propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedades-sub-eventos2', schema=AvroSchema(EventoPropiedadCreado))

        while True:
            mensaje = consumidor.receive()

            print(f'Evento recibido suscribirse_a_propiedad_creada: {mensaje.value().data}')
            eventoSaga = mensaje.value().data
            with app.app_context():
                fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
                repositorio = fabrica_repositorio.crear_objeto(RepositorioSagas.__class__)
                fabrica_sagas: Fabricasagas = Fabricasagas()
                saga2 =  fabrica_sagas.crear_objeto(repositorio.obtener_por_id(eventoSaga.id_cor), MapeadorSaga())
                saga2.id = eventoSaga.id_cor
                saga2.id_propiedad = eventoSaga.id_propiedad
                print(f'id de correlación: {saga2.id}')
                inquilino = json.loads(saga2.dataInquilino)
                comando = ComandoCrearInquilinoPayload(
                    nombres= inquilino["nombres"],
                    apellidos= inquilino["apellidos"],
                    id_cor= eventoSaga.id_cor,
                    identificacion = inquilino["identificacion"],
                    fecha_nacimiento = inquilino["fecha_nacimiento"],
                    genero= inquilino["genero"],
                    direccion= inquilino["direccion"],
                    telefono = inquilino["telefono"],
                    correo = inquilino["correo"]
                )

                UnidadTrabajoPuerto.limpiar()
                UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, saga2)
                UnidadTrabajoPuerto.savepoint()
                UnidadTrabajoPuerto.commit()
                despachador = Despachador()
                despachador.publicar_comando(comando, 'comandos2-inquilino')


            consumidor.acknowledge(mensaje)     

        saga.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if saga:
            saga.close()


def suscribirse_a_inquilino_creado(app):
    saga = None
    try:
        saga = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = saga.subscribe('eventos2-inquilino', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='inquilinos-sub-eventos2', schema=AvroSchema(EventoInquilinoCreado))

        while True:
            mensaje = consumidor.receive()
            eventoSaga = mensaje.value().data
            print(f'Evento recibido suscribirse_a_inquilino_creado: {mensaje.value().data}')

            with app.app_context():
                fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
                repositorio = fabrica_repositorio.crear_objeto(RepositorioSagas.__class__)
                fabrica_sagas: Fabricasagas = Fabricasagas()
                saga2 =  fabrica_sagas.crear_objeto(repositorio.obtener_por_id(eventoSaga.id_cor), MapeadorSaga())
                saga2.id = eventoSaga.id_cor
                saga2.id_inquilino = eventoSaga.id_inquilino

                UnidadTrabajoPuerto.limpiar()
                UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, saga2)
                UnidadTrabajoPuerto.savepoint()
                UnidadTrabajoPuerto.commit()
                
                comando = ComandoAsociarPropiedadPayload(
                    id_inquilino= saga2.id_inquilino,
                    id_propiedad= saga2.id_propiedad,
                    id_cor= eventoSaga.id_cor
                )

                despachador = Despachador()
                despachador.publicar_comando(comando, 'comandos3-inquilino')

            consumidor.acknowledge(mensaje)     

        saga.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if saga:
            saga.close()

def suscribirse_a_propiedad_asociada():
    saga = None
    try:
        saga = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = saga.subscribe('eventos-asociar-propiedad3', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='asociar-sub-eventos2', schema=AvroSchema(EventoPropiedadAsociada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido suscribirse_a_propiedad_asociada: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        saga.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if saga:
            saga.close()