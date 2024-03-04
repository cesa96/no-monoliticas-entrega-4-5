from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Propiedad(_message.Message):
    __slots__ = ["descripcion", "direccion", "disponible", "fecha_actualizacion", "fecha_construccion", "fecha_creacion", "fecha_modernizacion", "id", "metros_cuadrados", "nombre", "num_banos", "num_habitaciones", "precio", "servicios", "tipoPropiedad"]
    DESCRIPCION_FIELD_NUMBER: _ClassVar[int]
    DIRECCION_FIELD_NUMBER: _ClassVar[int]
    DISPONIBLE_FIELD_NUMBER: _ClassVar[int]
    FECHA_ACTUALIZACION_FIELD_NUMBER: _ClassVar[int]
    FECHA_CONSTRUCCION_FIELD_NUMBER: _ClassVar[int]
    FECHA_CREACION_FIELD_NUMBER: _ClassVar[int]
    FECHA_MODERNIZACION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    METROS_CUADRADOS_FIELD_NUMBER: _ClassVar[int]
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    NUM_BANOS_FIELD_NUMBER: _ClassVar[int]
    NUM_HABITACIONES_FIELD_NUMBER: _ClassVar[int]
    PRECIO_FIELD_NUMBER: _ClassVar[int]
    SERVICIOS_FIELD_NUMBER: _ClassVar[int]
    TIPOPROPIEDAD_FIELD_NUMBER: _ClassVar[int]
    descripcion: str
    direccion: str
    disponible: bool
    fecha_actualizacion: str
    fecha_construccion: str
    fecha_creacion: str
    fecha_modernizacion: str
    id: str
    metros_cuadrados: float
    nombre: str
    num_banos: int
    num_habitaciones: int
    precio: float
    servicios: str
    tipoPropiedad: str
    def __init__(self, id: _Optional[str] = ..., fecha_creacion: _Optional[str] = ..., fecha_actualizacion: _Optional[str] = ..., nombre: _Optional[str] = ..., descripcion: _Optional[str] = ..., num_habitaciones: _Optional[int] = ..., num_banos: _Optional[int] = ..., fecha_construccion: _Optional[str] = ..., fecha_modernizacion: _Optional[str] = ..., disponible: bool = ..., direccion: _Optional[str] = ..., precio: _Optional[float] = ..., metros_cuadrados: _Optional[float] = ..., tipoPropiedad: _Optional[str] = ..., servicios: _Optional[str] = ...) -> None: ...

class QueryPropiedad(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RespuestaPropiedad(_message.Message):
    __slots__ = ["mensaje", "propiedad"]
    MENSAJE_FIELD_NUMBER: _ClassVar[int]
    PROPIEDAD_FIELD_NUMBER: _ClassVar[int]
    mensaje: str
    propiedad: Propiedad
    def __init__(self, mensaje: _Optional[str] = ..., propiedad: _Optional[_Union[Propiedad, _Mapping]] = ...) -> None: ...
