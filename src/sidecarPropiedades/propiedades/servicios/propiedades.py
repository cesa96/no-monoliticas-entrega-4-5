import json
import requests
import datetime
import os

from propiedades.pb2py2.propiedades_pb2 import Propiedad, RespuestaPropiedad
from propiedades.pb2py2.propiedades_pb2_grpc import PropiedadesServicer


from google.protobuf.json_format import MessageToDict
from google.protobuf.timestamp_pb2 import Timestamp

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

class Propiedades(PropiedadesServicer):
    HOSTNAME_ENV: str = 'PROPIEDADES_ADDRESS'
    REST_API_HOST: str = f'http://{os.getenv(HOSTNAME_ENV, default="localhost")}:5003'
    REST_API_ENDPOINT: str = '/propiedades/propiedades'

    def CrearPropiedad(self, request, context):
        dict_obj = MessageToDict(request, preserving_proto_field_name=True)

        r = requests.post(f'{self.REST_API_HOST}{self.REST_API_ENDPOINT}', json=dict_obj)
        if r.status_code == 201:
            respuesta = json.loads(r.text)

            #fecha_creacion_dt = datetime.datetime.strptime(respuesta['fecha_creacion'], TIMESTAMP_FORMAT)
            #fecha_creacion = Timestamp()
            #fecha_creacion.FromDatetime(fecha_creacion_dt)

            #fecha_actualizacion_dt = datetime.datetime.strptime(respuesta['fecha_actualizacion'], TIMESTAMP_FORMAT)
            #fecha_actualizacion = Timestamp()
            #fecha_actualizacion.FromDatetime(fecha_actualizacion_dt)

            # propiedad =  Propiedad(id=respuesta.get('id'), 
            #     fecha_actualizacion=fecha_actualizacion, 
            #     fecha_creacion=fecha_creacion,
            #     nombre=respuesta.get('nombre'), 
            #     descripcion=respuesta.get('descripcion'), 
            #     num_habitaciones=respuesta.get('num_habitaciones'), 
            #     fecha_construccion=respuesta.get('fecha_construccion'), 
            #     disponible=respuesta.get('disponible'), 
            #     direccion=respuesta.get('direccion'), 
            #     precio=respuesta.get('precio'), 
            #     metros_cuadrados=respuesta.get('metros_cuadrados'), 
            #     tipoPropiedad=respuesta.get('tipoPropiedad'), 
            #     servicios=respuesta.get('servicios')
            #     )

            return RespuestaPropiedad(mensaje='OK', propiedad=None)
        else:
            return RespuestaPropiedad(mensaje=f'Error: {r.status_code}')

    def ConsultarPropiedad(self, id, context):
        dict_obj = MessageToDict(id, preserving_proto_field_name=True)
        r = requests.get(f'{self.REST_API_HOST}{self.REST_API_ENDPOINT}/{dict_obj.get("id")}')
        if r.status_code == 200:
            respuesta = json.loads(r.text)

            # fecha_creacion_dt = datetime.datetime.strptime(respuesta['fecha_creacion'], TIMESTAMP_FORMAT)
            # fecha_creacion = Timestamp()
            # fecha_creacion.FromDatetime(fecha_creacion_dt)

            # fecha_actualizacion_dt = datetime.datetime.strptime(respuesta['fecha_actualizacion'], TIMESTAMP_FORMAT)
            # fecha_actualizacion = Timestamp()
            # fecha_actualizacion.FromDatetime(fecha_actualizacion_dt)

            propiedad =  Propiedad(id=respuesta.get('id'), 
                fecha_actualizacion=respuesta['fecha_actualizacion'], 
                fecha_creacion=respuesta['fecha_creacion'],
                nombre=respuesta.get('nombre'), 
                descripcion=respuesta.get('descripcion'), 
                num_habitaciones=respuesta.get('num_habitaciones'), 
                fecha_construccion=respuesta.get('fecha_construccion'), 
                disponible=respuesta.get('disponible'), 
                direccion=respuesta.get('direccion'), 
                precio=respuesta.get('precio'), 
                metros_cuadrados=respuesta.get('metros_cuadrados'), 
                tipoPropiedad=respuesta.get('tipoPropiedad'), 
                servicios=respuesta.get('servicios')
                )

            return RespuestaPropiedad(mensaje='OK', propiedad=propiedad)
        else:
            return RespuestaPropiedad(mensaje=f'Error: {r.status_code}')