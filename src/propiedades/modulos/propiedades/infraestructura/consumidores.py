import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from inquilinos.modulos.inquilinos.infraestructura.schema.v1.comandos import ComandoEliminarInquilino
from propiedades.modulos.propiedades.aplicacion.comandos import eliminar_propiedad
from propiedades.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedades.modulos.propiedades.dominio.eventos import PropiedadCreadoFallo
from propiedades.modulos.propiedades.infraestructura.despachadores import Despachador

from propiedades.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreado
from propiedades.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando
from propiedades.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    propiedad = None
    try:
        propiedad = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = propiedad.subscribe('eventos2-propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedades-sub-eventos', schema=AvroSchema(EventoPropiedadCreado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        propiedad.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if propiedad:
            propiedad.close()

def suscribirse_a_comandos(app):
    propiedad = None
    try:
        propiedad = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = propiedad.subscribe('comandos2-propiedad', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedades-sub-comandos', schema=AvroSchema(ComandoCrearPropiedad))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            comandoPropiedad = mensaje.value().data
            try:

                comando = CrearPropiedad(comandoPropiedad.fecha_creacion,
                    comandoPropiedad.fecha_actualizacion,
                    comandoPropiedad.id,
                    comandoPropiedad.nombre,
                    comandoPropiedad.descripcion,
                    comandoPropiedad.id_cor,
                    comandoPropiedad.num_habitaciones,
                    comandoPropiedad.num_banos,
                    comandoPropiedad.fecha_construccion,
                    comandoPropiedad.fecha_modernizacion,
                    comandoPropiedad.disponible,
                    comandoPropiedad.direccion,
                    comandoPropiedad.precio,
                    comandoPropiedad.metrosCuadrados,
                    comandoPropiedad.tipoPropiedad,
                    comandoPropiedad.servicios)
                with app.app_context():
                    ejecutar_commando(comando)
            except:
                despachador = Despachador()
                despachador.publicar_evento(PropiedadCreadoFallo(id_cor=comandoPropiedad.id_cor), 'eventos-fallo-propiedad')
                logging.error('ERROR: Procesando comando crear propiedad!')
                traceback.print_exc()
                if propiedad:
                    propiedad.close()
            
        propiedad.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if propiedad:
            propiedad.close()

    

def suscribirse_a_comandos_eliminar(app):
    propiedad = None
    try:
        propiedad = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = propiedad.subscribe('comandos3-propiedad', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedad-sub-comandos3', schema=AvroSchema(ComandoEliminarInquilino))

        while True:
            mensaje = consumidor.receive()

            comandoPropiedad = mensaje.value().data
            comando = eliminar_propiedad(comandoPropiedad.id_propiedad,
                comandoPropiedad.id_cor)
            
            with app.app_context():
                ejecutar_commando(comando)

            consumidor.acknowledge(mensaje)     
            
        inquilino.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if propiedad:
            propiedad.close()
            consumidor.acknowledge(mensaje)     
