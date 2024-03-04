from concurrent import futures
import logging

import grpc
from inquilinos.pb2py2 import inquilinos_pb2
from inquilinos.pb2py2 import inquilinos_pb2_grpc


from inquilinos.servicios.inquilinos import Inquilinos

def agregar_servicios(servidor):
    inquilinos_pb2_grpc.add_InquilinosServicer_to_server(Inquilinos(), servidor)

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