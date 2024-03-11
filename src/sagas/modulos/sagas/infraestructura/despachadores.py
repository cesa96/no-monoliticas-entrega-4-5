import pulsar
from pulsar.schema import *

from sagas.modulos.sagas.infraestructura.schema.v1.eventos import EventoSagaCreado, SagaCreadoPayload
from sagas.modulos.sagas.infraestructura.schema.v1.comandos import ComandoAsociarPropiedadPayload, ComandoCrearInquilinoPayload, ComandoCrearPropiedadPayload, ComandoCrearSaga, ComandoCrearSagaPayload, ComandoCrearInquilino, ComandoCrearPropiedad, ComandoAsociarPropiedad, ComandoEliminarInquilino, ComandoEliminarPropiedad
from sagas.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        saga = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = saga.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        saga.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = SagaCreadoPayload(
            id_saga=str(evento.id_saga), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoSagaCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoSagaCreado))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        if topico == 'comandos-saga':
            payload = ComandoCrearSagaPayload(
                fecha_creacion = comando.fecha_creacion ,
                fecha_actualizacion = comando.fecha_actualizacion ,
                id = comando.id ,
                id_inquilino =     comando.id_inquilino,
                id_propiedad =     comando.id_propiedad,
                dataInquilino =     comando.dataInquilino,
                dataPropiedad =     comando.dataPropiedad
            )
            comando_integracion = ComandoCrearSaga(data=payload)
            self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearSaga))

        if topico == 'comandos2-propiedad':
            payload = ComandoCrearPropiedadPayload(
                fecha_creacion=str(comando.fecha_creacion),
                fecha_actualizacion=str(comando.fecha_actualizacion),
                id=str(comando.id),
                nombre=str(comando.nombre),
                descripcion=str(comando.descripcion),
                id_cor=str(comando.id_cor),
                num_habitaciones=int(comando.num_habitaciones),
                num_banos=int(comando.num_banos),
                fecha_construccion=str(comando.fecha_construccion),
                fecha_modernizacion=str(comando.fecha_modernizacion),
                disponible=bool(comando.disponible),
                direccion=str(comando.direccion),
                precio=float(comando.precio),
                metrosCuadrados=float(comando.metrosCuadrados),
                tipoPropiedad=str(comando.tipoPropiedad),
                servicios=str(comando.servicios)
            )
            comando_integracion = ComandoCrearPropiedad(data=payload)
            self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))

        if topico == 'comandos2-inquilino':
            payload = ComandoCrearInquilinoPayload(
                    fecha_actualizacion = str(comando.fecha_actualizacion),
                    id= str(comando.id),
                    nombres= str(comando.nombres),
                    apellidos= str(comando.apellidos),
                    identificacion= str(comando.identificacion),
                    fecha_nacimiento = str(comando.fecha_nacimiento),
                    id_cor=str(comando.id_cor),
                    genero= str(comando.genero),
                    direccion= str(comando.direccion),
                    telefono= str(comando.telefono),
                    correo= str(comando.correo),
                    sitioWeb= str(comando.sitioWeb))
            comando_integracion = ComandoCrearInquilino(data=payload)
            self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearInquilino))
        if topico == 'comandos3-inquilino':
            payload = ComandoAsociarPropiedadPayload(id_inquilino=str(comando.id_inquilino),
                                                     id_propiedad=str(comando.id_propiedad),
                                                     id_cor =str(comando.id_cor))
            comando_integracion = ComandoAsociarPropiedad(data=payload)


            self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoAsociarPropiedad))

        if topico == 'comandos4-inquilino':
            comando_integracion = ComandoEliminarInquilino(data=comando)
            self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoEliminarInquilino))

        if topico == 'comandos3-propiedad':
            comando_integracion = ComandoEliminarPropiedad(data=comando)
            self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoEliminarPropiedad))

