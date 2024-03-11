import pulsar
from pulsar.schema import *

from inquilinos.modulos.inquilinos.infraestructura.schema.v1.eventos import EventoInquilinoCreado, EventoInquilinoCreadoFallo, EventoInquilinoEliminado, InquilinoCreadoFalloPayload, InquilinoCreadoPayload, InquilinoEliminadoPayload, PropiedadAsociadaPayload, EventoPropiedadAsociada
from inquilinos.modulos.inquilinos.infraestructura.schema.v1.comandos import ComandoCrearInquilino, ComandoCrearInquilinoPayload, ComandoAsociarPropiedad, ComandoAsociarPropiedadPayload
from inquilinos.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        inquilino = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = inquilino.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        inquilino.close()


    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        if topico == 'eventos2-inquilino':
            payload = InquilinoCreadoPayload(
                id_inquilino=str(evento.id_inquilino), 
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion)),
                id_cor = str(evento.id_cor)
            )
            evento_integracion = EventoInquilinoCreado(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoInquilinoCreado))
        if topico == 'eventos-asociar-propiedad3':
            payload = PropiedadAsociadaPayload(
                id_inquilino=str(evento.id_inquilino),
                id_propiedad = str(evento.id_propiedad), 
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion)),
                id_cor = str(evento.id_cor)
            )
            evento_integracion = EventoPropiedadAsociada(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoPropiedadAsociada))
        if topico == 'eventos-eliminar-inquilino':
            payload = InquilinoEliminadoPayload(
                id_inquilino=str(evento.id_inquilino), 
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion)),
                id_cor = str(evento.id_cor)
            )
            evento_integracion = EventoInquilinoEliminado(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoInquilinoEliminado))
    
        if topico == 'eventos-fallo-inquilino' or topico == 'eventos-fallo-asociar':
            payload = InquilinoCreadoFalloPayload(
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion)),
                id_cor = str(evento.id_cor)
            )
            evento_integracion = EventoInquilinoCreadoFallo(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(InquilinoCreadoFalloPayload))


    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando

        if topico == "comandos2-inquilino":
            payload = ComandoCrearInquilinoPayload(
                    fecha_actualizacion = str(comando.fecha_actualizacion),
                    id= str(comando.id),
                    nombre= str(comando.nombre),
                    descripcion= str(comando.descripcion),
                    num_habitaciones= str(comando.num_habitaciones),
                    num_banos = str(comando.num_banos),
                    fecha_construccion= str(comando.fecha_construccion),
                    fecha_modernizacion= str(comando.fecha_modernizacion),
                    disponible= str(comando.disponible),
                    direccion= str(comando.direccion),
                    precio= str(comando.precio),
                    metrosCuadrados= str(comando.metrosCuadrados),
                    tipoPropiedad= str(comando.tipoPropiedad),
                    servicios= str(comando.servicios)
            )
            comando_integracion = ComandoCrearInquilino(data=payload)
            self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearInquilino))

        if topico == "comandos3-inquilino":
            payload = ComandoAsociarPropiedadPayload(id_inquilino=str(comando.id_inquilino),
                                                     id_propiedad=str(comando.id_propiedad),
                                                     id_cor =str(comando.id_cor))
            comando_integracion = ComandoAsociarPropiedad(data=payload)

            self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoAsociarPropiedad))
