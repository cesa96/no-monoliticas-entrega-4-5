# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import propiedades_pb2 as propiedades__pb2


class PropiedadesStub(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CrearPropiedad = channel.unary_unary(
                '/propiedades.Propiedades/CrearPropiedad',
                request_serializer=propiedades__pb2.Propiedad.SerializeToString,
                response_deserializer=propiedades__pb2.RespuestaPropiedad.FromString,
                )
        self.ConsultarPropiedad = channel.unary_unary(
                '/propiedades.Propiedades/ConsultarPropiedad',
                request_serializer=propiedades__pb2.QueryPropiedad.SerializeToString,
                response_deserializer=propiedades__pb2.RespuestaPropiedad.FromString,
                )


class PropiedadesServicer(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    def CrearPropiedad(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsultarPropiedad(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PropiedadesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CrearPropiedad': grpc.unary_unary_rpc_method_handler(
                    servicer.CrearPropiedad,
                    request_deserializer=propiedades__pb2.Propiedad.FromString,
                    response_serializer=propiedades__pb2.RespuestaPropiedad.SerializeToString,
            ),
            'ConsultarPropiedad': grpc.unary_unary_rpc_method_handler(
                    servicer.ConsultarPropiedad,
                    request_deserializer=propiedades__pb2.QueryPropiedad.FromString,
                    response_serializer=propiedades__pb2.RespuestaPropiedad.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'propiedades.Propiedades', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Propiedades(object):
    """------------------------------
    Servicios
    ------------------------------

    """

    @staticmethod
    def CrearPropiedad(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/propiedades.Propiedades/CrearPropiedad',
            propiedades__pb2.Propiedad.SerializeToString,
            propiedades__pb2.RespuestaPropiedad.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConsultarPropiedad(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/propiedades.Propiedades/ConsultarPropiedad',
            propiedades__pb2.QueryPropiedad.SerializeToString,
            propiedades__pb2.RespuestaPropiedad.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
