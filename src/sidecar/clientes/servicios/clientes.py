import json
import requests
import datetime
import os

from clientes.pb2py2.clientes_pb2 import Cliente, RespuestaCliente
from clientes.pb2py2.clientes_pb2_grpc import ClientesServicer


from google.protobuf.json_format import MessageToDict
from google.protobuf.timestamp_pb2 import Timestamp

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

class Vuelos(ClientesServicer):
    HOSTNAME_ENV: str = 'CLIENTES_ADDRESS'
    REST_API_HOST: str = f'http://{os.getenv(HOSTNAME_ENV, default="localhost")}:5000'
    REST_API_ENDPOINT: str = '/clientes'

    def CrearCliente(self, request, context):
        dict_obj = MessageToDict(request, preserving_proto_field_name=True)

        r = requests.post(f'{self.REST_API_HOST}{self.REST_API_ENDPOINT}', json=dict_obj)
        if r.status_code == 201:
            respuesta = json.loads(r.text)

            fecha_creacion_dt = datetime.datetime.strptime(respuesta['fecha_creacion'], TIMESTAMP_FORMAT)
            fecha_creacion = Timestamp()
            fecha_creacion.FromDatetime(fecha_creacion_dt)

            fecha_actualizacion_dt = datetime.datetime.strptime(respuesta['fecha_actualizacion'], TIMESTAMP_FORMAT)
            fecha_actualizacion = Timestamp()
            fecha_actualizacion.FromDatetime(fecha_actualizacion_dt)

            cliente =  Cliente(id=respuesta.get('id'), 
                fecha_actualizacion=fecha_actualizacion, 
                fecha_creacion=fecha_creacion,
                nombres=respuesta.get('nombres'), 
                apellidos=respuesta.get('apellidos'), 
                identificacion=respuesta.get('identificacion'), 
                fecha_nacimiento=respuesta.get('fecha_nacimiento'), 
                genero=respuesta.get('genero'), 
                direccion=respuesta.get('direccion'), 
                telefono=respuesta.get('telefono'), 
                correo=respuesta.get('correo'), 
                tipoCliente=respuesta.get('tipoCliente'), 
                sitioWeb=respuesta.get('sitioWeb')
                )

            return RespuestaCliente(mensaje='OK', cliente=cliente)
        else:
            return RespuestaCliente(mensaje=f'Error: {r.status_code}')

    def ConsultarCliente(self, id, context):
        r = requests.get(f'{self.REST_API_HOST}{self.REST_API_ENDPOINT}/{id}')
        if r.status_code == 200:
            respuesta = json.loads(r.text)

            fecha_creacion_dt = datetime.datetime.strptime(respuesta['fecha_creacion'], TIMESTAMP_FORMAT)
            fecha_creacion = Timestamp()
            fecha_creacion.FromDatetime(fecha_creacion_dt)

            fecha_actualizacion_dt = datetime.datetime.strptime(respuesta['fecha_actualizacion'], TIMESTAMP_FORMAT)
            fecha_actualizacion = Timestamp()
            fecha_actualizacion.FromDatetime(fecha_actualizacion_dt)

            cliente =  Cliente(id=respuesta.get('id'), 
                fecha_actualizacion=fecha_actualizacion, 
                fecha_creacion=fecha_creacion,
                nombres=respuesta.get('nombres'), 
                apellidos=respuesta.get('apellidos'), 
                identificacion=respuesta.get('identificacion'), 
                fecha_nacimiento=respuesta.get('fecha_nacimiento'), 
                genero=respuesta.get('genero'), 
                direccion=respuesta.get('direccion'), 
                telefono=respuesta.get('telefono'), 
                correo=respuesta.get('correo'), 
                tipoCliente=respuesta.get('tipoCliente'), 
                sitioWeb=respuesta.get('sitioWeb')
                )

            return RespuestaCliente(mensaje='OK', cliente=cliente)
        else:
            return RespuestaCliente(mensaje=f'Error: {r.status_code}')