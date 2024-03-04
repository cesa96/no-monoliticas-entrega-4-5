from concurrent import futures
import logging

import grpc
from propiedades.pb2py2 import propiedades_pb2
from propiedades.pb2py2 import propiedades_pb2_grpc


from propiedades.servicios.propiedades import Propiedades

def agregar_servicios(servidor):
    propiedades_pb2_grpc.add_PropiedadesServicer_to_server(Propiedades(), servidor)

def serve():
    port = '50053'
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agregar_servicios(servidor)

    servidor.add_insecure_port('[::]:' + port)
    servidor.start()
    print("Servidor corriendo por el puerto:" + port)
    servidor.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()