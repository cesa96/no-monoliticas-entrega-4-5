from concurrent import futures
import logging

import grpc
from clientes.pb2py2 import clientes_pb2
from clientes.pb2py2 import clientes_pb2_grpc


from sidecar.clientes.servicios.clientes import Clientes

def agregar_servicios(servidor):
    clientes_pb2_grpc.add_ClientesServicer_to_server(Clientes(), servidor)

def serve():
    port = '50051'
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agregar_servicios(servidor)

    servidor.add_insecure_port('[::]:' + port)
    servidor.start()
    print("Servidor corriendo por el puerto:" + port)
    servidor.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()