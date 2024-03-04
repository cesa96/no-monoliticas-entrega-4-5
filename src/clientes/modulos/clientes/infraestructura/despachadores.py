import pulsar
from pulsar.schema import *

from clientes.modulos.clientes.infraestructura.schema.v1.eventos import EventoClienteCreado, ClienteCreadoPayload
from clientes.modulos.clientes.infraestructura.schema.v1.comandos import ComandoCrearCliente, ComandoCrearClientePayload
from clientes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ClienteCreadoPayload(
            id_cliente=str(evento.id_cliente), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoClienteCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoClienteCreado))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearClientePayload(
            fecha_creacion = comando.fecha_creacion ,
            fecha_actualizacion = comando.fecha_actualizacion ,
            id = comando.id ,
            nombres = comando.nombres ,
            apellidos = comando.apellidos ,
            identificacion = comando.identificacion ,
            fecha_nacimiento = comando.identificacion ,
            genero = comando.genero ,
            direccion = comando.direccion ,
            telefono = comando.telefono ,
            correo = comando.correo ,
            tipoCliente = comando.tipoCliente ,
            sitioWeb = comando.sitioWeb 
        )
        
        comando_integracion = ComandoCrearCliente(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearCliente))
