import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from propiedades.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreado
from propiedades.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad
from propiedades.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    propiedad = None
    try:
        propiedad = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = propiedad.subscribe('eventos-propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedades-sub-eventos', schema=AvroSchema(EventoPropiedadCreado))

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

def suscribirse_a_comandos():
    propiedad = None
    try:
        propiedad = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = propiedad.subscribe('comandos-propiedad', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedades-sub-comandos', schema=AvroSchema(ComandoCrearPropiedad))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        propiedad.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if propiedad:
            propiedad.close()