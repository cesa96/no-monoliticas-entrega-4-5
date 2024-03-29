# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import inquilinos_pb2 as inquilinos__pb2


class InquilinosStub(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CrearInquilino = channel.unary_unary(
                '/inquilinos.Inquilinos/CrearInquilino',
                request_serializer=inquilinos__pb2.Inquilino.SerializeToString,
                response_deserializer=inquilinos__pb2.RespuestaInquilino.FromString,
                )
        self.ConsultarInquilino = channel.unary_unary(
                '/inquilinos.Inquilinos/ConsultarInquilino',
                request_serializer=inquilinos__pb2.QueryInquilino.SerializeToString,
                response_deserializer=inquilinos__pb2.RespuestaInquilino.FromString,
                )
        self.AsociarPropiedad = channel.unary_unary(
                '/inquilinos.Inquilinos/AsociarPropiedad',
                request_serializer=inquilinos__pb2.PropiedadInquilino.SerializeToString,
                response_deserializer=inquilinos__pb2.RespuestaInquilino.FromString,
                )


class InquilinosServicer(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    def CrearInquilino(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsultarInquilino(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AsociarPropiedad(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InquilinosServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CrearInquilino': grpc.unary_unary_rpc_method_handler(
                    servicer.CrearInquilino,
                    request_deserializer=inquilinos__pb2.Inquilino.FromString,
                    response_serializer=inquilinos__pb2.RespuestaInquilino.SerializeToString,
            ),
            'ConsultarInquilino': grpc.unary_unary_rpc_method_handler(
                    servicer.ConsultarInquilino,
                    request_deserializer=inquilinos__pb2.QueryInquilino.FromString,
                    response_serializer=inquilinos__pb2.RespuestaInquilino.SerializeToString,
            ),
            'AsociarPropiedad': grpc.unary_unary_rpc_method_handler(
                    servicer.AsociarPropiedad,
                    request_deserializer=inquilinos__pb2.PropiedadInquilino.FromString,
                    response_serializer=inquilinos__pb2.RespuestaInquilino.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'inquilinos.Inquilinos', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Inquilinos(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    @staticmethod
    def CrearInquilino(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inquilinos.Inquilinos/CrearInquilino',
            inquilinos__pb2.Inquilino.SerializeToString,
            inquilinos__pb2.RespuestaInquilino.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConsultarInquilino(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inquilinos.Inquilinos/ConsultarInquilino',
            inquilinos__pb2.QueryInquilino.SerializeToString,
            inquilinos__pb2.RespuestaInquilino.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AsociarPropiedad(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inquilinos.Inquilinos/AsociarPropiedad',
            inquilinos__pb2.PropiedadInquilino.SerializeToString,
            inquilinos__pb2.RespuestaInquilino.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
