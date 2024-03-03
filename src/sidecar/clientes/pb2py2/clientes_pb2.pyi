from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cliente(_message.Message):
    __slots__ = ["apellidos", "correo", "direccion", "fecha_actualizacion", "fecha_creacion", "fecha_nacimiento", "genero", "id", "identificacion", "nombres", "sitioWeb", "telefono", "tipoCliente"]
    APELLIDOS_FIELD_NUMBER: _ClassVar[int]
    CORREO_FIELD_NUMBER: _ClassVar[int]
    DIRECCION_FIELD_NUMBER: _ClassVar[int]
    FECHA_ACTUALIZACION_FIELD_NUMBER: _ClassVar[int]
    FECHA_CREACION_FIELD_NUMBER: _ClassVar[int]
    FECHA_NACIMIENTO_FIELD_NUMBER: _ClassVar[int]
    GENERO_FIELD_NUMBER: _ClassVar[int]
    IDENTIFICACION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NOMBRES_FIELD_NUMBER: _ClassVar[int]
    SITIOWEB_FIELD_NUMBER: _ClassVar[int]
    TELEFONO_FIELD_NUMBER: _ClassVar[int]
    TIPOCLIENTE_FIELD_NUMBER: _ClassVar[int]
    apellidos: str
    correo: str
    direccion: str
    fecha_actualizacion: str
    fecha_creacion: str
    fecha_nacimiento: str
    genero: str
    id: str
    identificacion: str
    nombres: str
    sitioWeb: str
    telefono: str
    tipoCliente: str
    def __init__(self, id: _Optional[str] = ..., fecha_creacion: _Optional[str] = ..., fecha_actualizacion: _Optional[str] = ..., nombres: _Optional[str] = ..., apellidos: _Optional[str] = ..., identificacion: _Optional[str] = ..., fecha_nacimiento: _Optional[str] = ..., genero: _Optional[str] = ..., direccion: _Optional[str] = ..., telefono: _Optional[str] = ..., correo: _Optional[str] = ..., tipoCliente: _Optional[str] = ..., sitioWeb: _Optional[str] = ...) -> None: ...

class QueryCliente(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RespuestaCliente(_message.Message):
    __slots__ = ["cliente", "mensaje"]
    CLIENTE_FIELD_NUMBER: _ClassVar[int]
    MENSAJE_FIELD_NUMBER: _ClassVar[int]
    cliente: Cliente
    mensaje: str
    def __init__(self, mensaje: _Optional[str] = ..., cliente: _Optional[_Union[Cliente, _Mapping]] = ...) -> None: ...
