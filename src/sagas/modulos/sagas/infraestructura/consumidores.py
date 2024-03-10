import json
import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from sagas.modulos.sagas.infraestructura.despachadores import Despachador
from sagas.config import db
from sagas.modulos.sagas.aplicacion.comandos.crear_saga import CrearSaga
from sagas.modulos.sagas.dominio.fabricas import Fabricasagas
from sagas.modulos.sagas.dominio.repositorios import RepositorioSagas
from sagas.modulos.sagas.infraestructura.fabricas import FabricaRepositorio
from sagas.modulos.sagas.infraestructura.mapeadores import MapeadorSaga

from sagas.modulos.sagas.infraestructura.schema.v1.eventos import EventoSagaCreado
from sagas.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearSaga, ComandoCrearInquilino, ComandoCrearPropiedad, ComandoAsociarPropiedad, ComandoAsociarPropiedadPayload, ComandoCrearInquilinoPayload, ComandoCrearPropiedadPayload
from sagas.seedwork.aplicacion.comandos import ejecutar_commando
from sagas.seedwork.infraestructura import utils

def suscribirse_a_eventos(app):
    saga = None
    try:
        saga = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = saga.subscribe('eventos-saga', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='sagas-sub-eventos2', schema=AvroSchema(EventoSagaCreado))

        while True:
            mensaje = consumidor.receive()

            eventoSaga = mensaje.value().data
            with app.app_context():
                fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
                repositorio = fabrica_repositorio.crear_objeto(RepositorioSagas.__class__)
                fabrica_sagas: Fabricasagas = Fabricasagas()
                saga2 =  fabrica_sagas.crear_objeto(repositorio.obtener_por_id(eventoSaga.id_saga), MapeadorSaga())
                propiedad = json.loads(saga2.dataPropiedad)


                comando = ComandoCrearPropiedadPayload(
                    nombre= propiedad["nombre"],
                    descripcion= propiedad["descripcion"],
                    id_cor= eventoSaga.id_saga,
                    num_habitaciones = int(propiedad["num_habitaciones"]),
                    num_banos = int(propiedad["num_banos"]),
                    fecha_construccion= propiedad["fecha_construccion"],
                    fecha_modernizacion= propiedad["fecha_modernizacion"],
                    disponible = propiedad["disponible"],
                    direccion = propiedad["direccion"],
                    precio = float(propiedad["precio"]),
                    metrosCuadrados = float(propiedad["metros_cuadrados"]),
                    tipoPropiedad= propiedad["tipoPropiedad"],
                    servicios= propiedad["servicios"]
                )

                despachador = Despachador()
                despachador.publicar_comando(comando, 'comandos2-propiedad')



            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        saga.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if saga:
            saga.close()

def suscribirse_a_comandos(app):
    saga = None
    try:
        saga = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = saga.subscribe('comandos-saga', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='sagas-sub-comandos2', schema=AvroSchema(ComandoCrearSaga))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            comandoSaga = mensaje.value().data
            comando = CrearSaga(comandoSaga.fecha_creacion,
                comandoSaga.fecha_actualizacion,
                comandoSaga.id,
                comandoSaga.id_inquilino,
                comandoSaga.id_propiedad,
                comandoSaga.dataInquilino,
                comandoSaga.dataPropiedad
                )
            
            with app.app_context():
                ejecutar_commando(comando)


            consumidor.acknowledge(mensaje)     
            
        saga.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if saga:
            saga.close()