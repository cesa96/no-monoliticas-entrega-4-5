import pulsar
from pulsar.schema import *

from propiedades.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreado, PropiedadCreadoPayload
from propiedades.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload
from propiedades.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        propiedad = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = propiedad.create_producer(topico, schema=AvroSchema(EventoPropiedadCreado))
        publicador.send(mensaje)
        propiedad.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = PropiedadCreadoPayload(
            id_propiedad=str(evento.id_propiedad), 
            id_cor = str(evento.id_cor),
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoPropiedadCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoPropiedadCreado))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando



        payload = ComandoCrearPropiedadPayload(
                fecha_creacion=str(comando.fecha_creacion),
                fecha_actualizacion=str(comando.fecha_actualizacion),
                id=str(comando.id),
                nombre=str(comando.nombre),
                descripcion=str(comando.descripcion),
                id_cor=str(comando.id_cor),
                num_habitaciones=str(comando.num_habitaciones),
                num_banos=str(comando.num_banos),
                fecha_construccion=str(comando.fecha_construccion),
                fecha_modernizacion=str(comando.fecha_modernizacion),
                disponible=str(comando.disponible),
                direccion=str(comando.direccion),
                precio=str(comando.precio),
                metrosCuadrados=str(comando.metrosCuadrados),
                tipoPropiedad=str(comando.tipoPropiedad),
                servicios=str(comando.servicios)
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))
