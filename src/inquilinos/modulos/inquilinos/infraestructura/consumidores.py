import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from inquilinos.modulos.inquilinos.infraestructura.schema.v1.eventos import EventoInquilinoCreado
from inquilinos.modulos.inquilinos.infraestructura.schema.v1.comandos import ComandoCrearInquilino
from inquilinos.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    inquilino = None
    try:
        inquilino = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = inquilino.subscribe('eventos-inquilino', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='inquilinos-sub-eventos', schema=AvroSchema(EventoInquilinoCreado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        inquilino.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if inquilino:
            inquilino.close()

def suscribirse_a_comandos():
    inquilino = None
    try:
        inquilino = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = inquilino.subscribe('comandos-inquilino', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='inquilinos-sub-comandos', schema=AvroSchema(ComandoCrearInquilino))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        inquilino.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if inquilino:
            inquilino.close()