import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from inquilinos.modulos.inquilinos.aplicacion.comandos.crear_inquilino import CrearInquilino
from inquilinos.modulos.inquilinos.aplicacion.comandos.asociar_propiedad import AsociarPropiedad
from inquilinos.modulos.inquilinos.aplicacion.comandos.eliminar_inquilino import EliminarInquilino
from inquilinos.modulos.inquilinos.dominio.eventos import InquilinoCreadoFallo
from inquilinos.modulos.inquilinos.infraestructura.despachadores import Despachador

from inquilinos.modulos.inquilinos.infraestructura.schema.v1.eventos import EventoInquilinoCreado
from inquilinos.modulos.inquilinos.infraestructura.schema.v1.comandos import ComandoCrearInquilino, ComandoAsociarPropiedad, ComandoEliminarInquilino
from inquilinos.seedwork.aplicacion.comandos import ejecutar_commando
from inquilinos.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    inquilino = None
    try:
        inquilino = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = inquilino.subscribe('eventos2-inquilino', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='inquilinos-sub-eventos', schema=AvroSchema(EventoInquilinoCreado))

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

def suscribirse_a_comandos(app):
    inquilino = None
    try:
        inquilino = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = inquilino.subscribe('comandos2-inquilino', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='inquilinos-sub-comandos', schema=AvroSchema(ComandoCrearInquilino))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            comandoPropiedad = mensaje.value().data
            try:
                comando = CrearInquilino(comandoPropiedad.fecha_creacion,
                    comandoPropiedad.fecha_actualizacion,
                    comandoPropiedad.id,
                    comandoPropiedad.nombres,
                    comandoPropiedad.apellidos,
                    comandoPropiedad.identificacion,
                    comandoPropiedad.fecha_nacimiento,
                    comandoPropiedad.genero,
                    comandoPropiedad.id_cor,
                    comandoPropiedad.direccion,
                    comandoPropiedad.telefono,
                    comandoPropiedad.correo,
                    comandoPropiedad.sitioWeb)
                comando.id = None
                
                with app.app_context():
                    ejecutar_commando(comando)

                consumidor.acknowledge(mensaje)     
            except:
                despachador = Despachador()
                despachador.publicar_evento(InquilinoCreadoFallo(id_cor=comandoPropiedad.id_cor), 'eventos-fallo-inquilino')
                logging.error('ERROR: Procesando comando crear inquilino!')
                traceback.print_exc()
                if inquilino:
                    inquilino.close()

        inquilino.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if inquilino:
            inquilino.close()

def suscribirse_a_comandos_asociar(app):
    inquilino = None
    try:
        inquilino = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = inquilino.subscribe('comandos3-inquilino', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='inquilinos-sub-comandos3', schema=AvroSchema(ComandoAsociarPropiedad))

        while True:
            mensaje = consumidor.receive()

            comandoPropiedad = mensaje.value().data
            try:
                comando = AsociarPropiedad(comandoPropiedad.id_inquilino,
                    comandoPropiedad.id_propiedad,comandoPropiedad.id_cor)
                
                with app.app_context():
                    ejecutar_commando(comando)

                consumidor.acknowledge(mensaje)     
            except:
                despachador = Despachador()
                despachador.publicar_evento(InquilinoCreadoFallo(id_cor=comandoPropiedad.id_cor), 'eventos-fallo-asociar')
                logging.error('ERROR: Procesando comando crear inquilino!')
                traceback.print_exc()
                if inquilino:
                    inquilino.close()
            
        inquilino.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if inquilino:
            inquilino.close()


def suscribirse_a_comandos_eliminar(app):
    inquilino = None
    try:
        inquilino = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = inquilino.subscribe('comandos4-inquilino', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='inquilinos-sub-comandos4', schema=AvroSchema(ComandoEliminarInquilino))

        while True:
            mensaje = consumidor.receive()

            comandoPropiedad = mensaje.value().data
            comando = EliminarInquilino(comandoPropiedad.id_inquilino,
                comandoPropiedad.id_cor)
            
            with app.app_context():
                ejecutar_commando(comando)

            consumidor.acknowledge(mensaje)     
            
        inquilino.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if inquilino:
            inquilino.close()