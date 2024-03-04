from __future__ import print_function

from google.protobuf.timestamp_pb2 import Timestamp
from propiedades.pb2py2 import propiedades_pb2
from propiedades.pb2py2 import propiedades_pb2_grpc

import logging
import grpc
import datetime
import os
import json


def importar_comando_propiedad(json_file):
    json_dict = json.load(json_file)
    return json_dict

def dict_a_proto_propiedad(dict_propiedad):
    return propiedades_pb2.Propiedad(id=dict_propiedad.get('id'),
                                nombre=dict_propiedad.get('nombre'), 
                                descripcion=dict_propiedad.get('descripcion'), 
                                num_habitaciones=dict_propiedad.get('num_habitaciones'), 
                                fecha_construccion=dict_propiedad.get('fecha_construccion'), 
                                disponible=dict_propiedad.get('disponible'), 
                                direccion=dict_propiedad.get('direccion'), 
                                precio=dict_propiedad.get('precio'), 
                                metros_cuadrados=dict_propiedad.get('metros_cuadrados'), 
                                tipoPropiedad=dict_propiedad.get('tipoPropiedad'), 
                                servicios=dict_propiedad.get('servicios')
                                )

def run():

    print("Crear una propiedad")
    with grpc.insecure_channel('localhost:50053') as channel:
        json_file = open(f'{os.path.dirname(__file__)}/mensajes/crear_propiedad.json')
        json_dict = importar_comando_propiedad(json_file)
        propiedad = dict_a_proto_propiedad(json_dict)
        stub = propiedades_pb2_grpc.PropiedadesStub(channel)
        response = stub.CrearPropiedad(propiedad)

    print("Greeter client received: " + response.mensaje)
    print(f'Propiedad: {response.propiedad}')

    print("Consultar una propiedad")
    with grpc.insecure_channel('localhost:50053') as channel:

        par = propiedades_pb2.QueryPropiedad(id = "627c94a3-9bfb-4a33-a46f-8d94f4d54ef4")
        stub = propiedades_pb2_grpc.PropiedadesStub(channel)
        response = stub.ConsultarPropiedad(par)

    print("Greeter client received: " + response.mensaje)
    print(f'Propiedad: {response.propiedad}')


if __name__ == '__main__':
    logging.basicConfig()
    run()