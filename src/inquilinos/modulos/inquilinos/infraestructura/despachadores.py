import pulsar
from pulsar.schema import *

from inquilinos.modulos.inquilinos.infraestructura.schema.v1.eventos import EventoInquilinoCreado, InquilinoCreadoPayload
from inquilinos.modulos.inquilinos.infraestructura.schema.v1.comandos import ComandoCrearInquilino, ComandoCrearInquilinoPayload
from inquilinos.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        inquilino = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = inquilino.create_producer(topico, schema=AvroSchema(EventoInquilinoCreado))
        publicador.send(mensaje)
        inquilino.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = InquilinoCreadoPayload(
            id_inquilino=str(evento.id_inquilino), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoInquilinoCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoInquilinoCreado))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearInquilinoPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearInquilino(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearInquilino))
