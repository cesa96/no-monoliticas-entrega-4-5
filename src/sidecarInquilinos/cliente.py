from __future__ import print_function

from google.protobuf.timestamp_pb2 import Timestamp
from inquilinos.pb2py2 import inquilinos_pb2
from inquilinos.pb2py2 import inquilinos_pb2_grpc

import logging
import grpc
import datetime
import os
import json


def importar_comando_inquilino(json_file):
    json_dict = json.load(json_file)
    return json_dict

def dict_a_proto_inquilino(dict_inquilino):
    return inquilinos_pb2.Inquilino(id=dict_inquilino.get('id'),
                                nombres=dict_inquilino.get('nombres'), 
                                apellidos=dict_inquilino.get('apellidos'), 
                                identificacion=dict_inquilino.get('identificacion'), 
                                fecha_nacimiento=dict_inquilino.get('fecha_nacimiento'), 
                                genero=dict_inquilino.get('genero'), 
                                direccion=dict_inquilino.get('direccion'), 
                                telefono=dict_inquilino.get('telefono'), 
                                correo=dict_inquilino.get('correo'), 
                                sitioWeb=dict_inquilino.get('sitioWeb')
                                )

def run():

    print("Crear una inquilino")
    with grpc.insecure_channel('localhost:50051') as channel:
        json_file = open(f'{os.path.dirname(__file__)}/mensajes/crear_inquilino.json')
        json_dict = importar_comando_inquilino(json_file)
        inquilino = dict_a_proto_inquilino(json_dict)
        stub = inquilinos_pb2_grpc.InquilinosStub(channel)
        response = stub.CrearInquilino(inquilino)

    print("Greeter client received: " + response.mensaje)
    print(f'Inquilino: {response.inquilino}')

    print("Consultar una inquilino")
    with grpc.insecure_channel('localhost:50051') as channel:

        par = inquilinos_pb2.QueryInquilino(id = "32fe678b-9212-440a-a35f-740b570f7131")
        stub = inquilinos_pb2_grpc.InquilinosStub(channel)
        response = stub.ConsultarInquilino(par)
        
    print("Greeter client received: " + response.mensaje)
    print(f'Inquilino: {response.inquilino}')

    print("Asociar propiedad")
    with grpc.insecure_channel('localhost:50051') as channel:

        par = inquilinos_pb2.PropiedadInquilino(id_inquilino="32fe678b-9212-440a-a35f-740b570f7131", id_propiedad="cecec011-4920-46a5-b3a9-663d0d960039")
        stub = inquilinos_pb2_grpc.InquilinosStub(channel)
        response = stub.ConsultarInquilino(par)


if __name__ == '__main__':
    logging.basicConfig()
    run()