import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from clientes.config import db
from clientes.modulos.clientes.aplicacion.comandos.crear_cliente import CrearCliente

from clientes.modulos.clientes.infraestructura.schema.v1.eventos import EventoClienteCreado
from clientes.modulos.clientes.infraestructura.schema.v1.comandos import ComandoCrearCliente
from clientes.seedwork.aplicacion.comandos import ejecutar_commando
from clientes.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-cliente', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='clientes-sub-eventos', schema=AvroSchema(EventoClienteCreado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos2-cliente', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='clientes-sub-comandos', schema=AvroSchema(ComandoCrearCliente))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            comandoCliente = mensaje.value().data
            comando = CrearCliente(comandoCliente.fecha_creacion,
                comandoCliente.fecha_actualizacion,
                comandoCliente.id,
                comandoCliente.nombres,
                comandoCliente.apellidos,
                comandoCliente.identificacion,
                comandoCliente.fecha_nacimiento,
                comandoCliente.genero,
                comandoCliente.direccion,
                comandoCliente.telefono,
                comandoCliente.correo,
                comandoCliente.tipoCliente,
                comandoCliente.sitioWeb)
            
            with app.app_context():
                ejecutar_commando(comando)


            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()