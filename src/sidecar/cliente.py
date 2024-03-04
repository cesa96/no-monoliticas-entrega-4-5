from __future__ import print_function

from google.protobuf.timestamp_pb2 import Timestamp
from clientes.pb2py2 import clientes_pb2
from clientes.pb2py2 import clientes_pb2_grpc

import logging
import grpc
import datetime
import os
import json


def importar_comando_cliente(json_file):
    json_dict = json.load(json_file)
    return json_dict

def dict_a_proto_cliente(dict_cliente):
    return clientes_pb2.Cliente(id=dict_cliente.get('id'),
                                nombres=dict_cliente.get('nombres'), 
                                apellidos=dict_cliente.get('apellidos'), 
                                identificacion=dict_cliente.get('identificacion'), 
                                fecha_nacimiento=dict_cliente.get('fecha_nacimiento'), 
                                genero=dict_cliente.get('genero'), 
                                direccion=dict_cliente.get('direccion'), 
                                telefono=dict_cliente.get('telefono'), 
                                correo=dict_cliente.get('correo'), 
                                tipoCliente=dict_cliente.get('tipoCliente'), 
                                sitioWeb=dict_cliente.get('sitioWeb')
                                )

def run():

    print("Crear una cliente")
    with grpc.insecure_channel('localhost:50051') as channel:
        json_file = open(f'{os.path.dirname(__file__)}/mensajes/crear_cliente.json')
        json_dict = importar_comando_cliente(json_file)
        cliente = dict_a_proto_cliente(json_dict)
        stub = clientes_pb2_grpc.ClientesStub(channel)
        response = stub.CrearCliente(cliente)

    print("Greeter client received: " + response.mensaje)
    print(f'Cliente: {response.cliente}')

    print("Consultar una cliente")
    with grpc.insecure_channel('localhost:50051') as channel:

        par = clientes_pb2.QueryCliente(id = "cecec011-4920-46a5-b3a9-663d0d960039")
        stub = clientes_pb2_grpc.ClientesStub(channel)
        response = stub.ConsultarCliente(par)

    print("Greeter client received: " + response.mensaje)
    print(f'Cliente: {response.cliente}')


if __name__ == '__main__':
    logging.basicConfig()
    run()