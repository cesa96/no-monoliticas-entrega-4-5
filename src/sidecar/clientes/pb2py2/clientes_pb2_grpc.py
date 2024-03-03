# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import clientes_pb2 as clientes__pb2


class ClientesStub(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CrearCliente = channel.unary_unary(
                '/clientes.Clientes/CrearCliente',
                request_serializer=clientes__pb2.Cliente.SerializeToString,
                response_deserializer=clientes__pb2.RespuestaCliente.FromString,
                )
        self.ConsultarCliente = channel.unary_unary(
                '/clientes.Clientes/ConsultarCliente',
                request_serializer=clientes__pb2.QueryCliente.SerializeToString,
                response_deserializer=clientes__pb2.RespuestaCliente.FromString,
                )


class ClientesServicer(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    def CrearCliente(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsultarCliente(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CrearCliente': grpc.unary_unary_rpc_method_handler(
                    servicer.CrearCliente,
                    request_deserializer=clientes__pb2.Cliente.FromString,
                    response_serializer=clientes__pb2.RespuestaCliente.SerializeToString,
            ),
            'ConsultarCliente': grpc.unary_unary_rpc_method_handler(
                    servicer.ConsultarCliente,
                    request_deserializer=clientes__pb2.QueryCliente.FromString,
                    response_serializer=clientes__pb2.RespuestaCliente.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'clientes.Clientes', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Clientes(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    @staticmethod
    def CrearCliente(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clientes.Clientes/CrearCliente',
            clientes__pb2.Cliente.SerializeToString,
            clientes__pb2.RespuestaCliente.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConsultarCliente(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clientes.Clientes/ConsultarCliente',
            clientes__pb2.QueryCliente.SerializeToString,
            clientes__pb2.RespuestaCliente.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
