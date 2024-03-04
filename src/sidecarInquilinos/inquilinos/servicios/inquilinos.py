import json
import requests
import datetime
import os

from inquilinos.pb2py2.inquilinos_pb2 import Inquilino, PropiedadInquilino, RespuestaInquilino
from inquilinos.pb2py2.inquilinos_pb2_grpc import InquilinosServicer


from google.protobuf.json_format import MessageToDict
from google.protobuf.timestamp_pb2 import Timestamp

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

class Inquilinos(InquilinosServicer):
    HOSTNAME_ENV: str = 'INQUILINOS_ADDRESS'
    REST_API_HOST: str = f'http://{os.getenv(HOSTNAME_ENV, default="localhost")}:5002'
    REST_API_ENDPOINT: str = '/inquilinos/inquilinos'

    def CrearInquilino(self, request, context):
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

            # inquilino =  Inquilino(id=respuesta.get('id'), 
            #     fecha_actualizacion=fecha_actualizacion, 
            #     fecha_creacion=fecha_creacion,
            #     nombres=respuesta.get('nombres'), 
            #     apellidos=respuesta.get('apellidos'), 
            #     identificacion=respuesta.get('identificacion'), 
            #     fecha_nacimiento=respuesta.get('fecha_nacimiento'), 
            #     genero=respuesta.get('genero'), 
            #     direccion=respuesta.get('direccion'), 
            #     telefono=respuesta.get('telefono'), 
            #     correo=respuesta.get('correo'), 
            #     sitioWeb=respuesta.get('sitioWeb')
            #     )

            return RespuestaInquilino(mensaje='OK', inquilino=None)
        else:
            return RespuestaInquilino(mensaje=f'Error: {r.status_code}')

    def AsociarPropiedad(self, propiedadInquilino, context):
        dict_obj = MessageToDict(propiedadInquilino, preserving_proto_field_name=True)
        r = requests.put(f'{self.REST_API_HOST}{self.REST_API_ENDPOINT}/{dict_obj.get("id_inquilino")}/asociar_propiedad/{dict_obj.get("id_propiedad")}')
        if r.status_code == 200:
            respuesta = json.loads(r.text)

            # fecha_creacion_dt = datetime.datetime.strptime(respuesta['fecha_creacion'], TIMESTAMP_FORMAT)
            # fecha_creacion = Timestamp()
            # fecha_creacion.FromDatetime(fecha_creacion_dt)

            # fecha_actualizacion_dt = datetime.datetime.strptime(respuesta['fecha_actualizacion'], TIMESTAMP_FORMAT)
            # fecha_actualizacion = Timestamp()
            # fecha_actualizacion.FromDatetime(fecha_actualizacion_dt)

            return RespuestaInquilino(mensaje='OK', inquilino=None)
        else:
            return RespuestaInquilino(mensaje=f'Error: {r.status_code}')
        
    def ConsultarInquilino(self, id, context):
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

            propiedades = list()

            for propiedad in respuesta.get('propiedades'):
                prop = PropiedadInquilino(id=str(propiedad.get('id')), id_inquilino=str(respuesta.get('id')), id_propiedad = str(propiedad.get('id_propiedad')))
                propiedades.append(prop)

            inquilino =  Inquilino(id=respuesta.get('id'), 
                fecha_actualizacion=respuesta['fecha_actualizacion'], 
                fecha_creacion=respuesta['fecha_creacion'],
                nombres=respuesta.get('nombres'), 
                apellidos=respuesta.get('apellidos'), 
                identificacion=respuesta.get('identificacion'), 
                fecha_nacimiento=respuesta.get('fecha_nacimiento'), 
                genero=respuesta.get('genero'), 
                direccion=respuesta.get('direccion'), 
                telefono=respuesta.get('telefono'), 
                correo=respuesta.get('correo'), 
                sitioWeb=respuesta.get('sitioWeb'),
                propiedades = propiedades
                )

            return RespuestaInquilino(mensaje='OK', inquilino=inquilino)
        else:
            return RespuestaInquilino(mensaje=f'Error: {r.status_code}')