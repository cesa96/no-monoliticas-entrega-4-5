from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Inquilino(_message.Message):
    __slots__ = ["apellidos", "correo", "direccion", "fecha_actualizacion", "fecha_creacion", "fecha_nacimiento", "genero", "id", "identificacion", "nombres", "propiedades", "sitioWeb", "telefono"]
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
    PROPIEDADES_FIELD_NUMBER: _ClassVar[int]
    SITIOWEB_FIELD_NUMBER: _ClassVar[int]
    TELEFONO_FIELD_NUMBER: _ClassVar[int]
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
    propiedades: _containers.RepeatedCompositeFieldContainer[PropiedadInquilino]
    sitioWeb: str
    telefono: str
    def __init__(self, id: _Optional[str] = ..., fecha_creacion: _Optional[str] = ..., fecha_actualizacion: _Optional[str] = ..., nombres: _Optional[str] = ..., apellidos: _Optional[str] = ..., identificacion: _Optional[str] = ..., fecha_nacimiento: _Optional[str] = ..., genero: _Optional[str] = ..., direccion: _Optional[str] = ..., telefono: _Optional[str] = ..., correo: _Optional[str] = ..., sitioWeb: _Optional[str] = ..., propiedades: _Optional[_Iterable[_Union[PropiedadInquilino, _Mapping]]] = ...) -> None: ...

class PropiedadInquilino(_message.Message):
    __slots__ = ["id", "id_inquilino", "id_propiedad"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_INQUILINO_FIELD_NUMBER: _ClassVar[int]
    ID_PROPIEDAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    id_inquilino: str
    id_propiedad: str
    def __init__(self, id_inquilino: _Optional[str] = ..., id_propiedad: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class QueryInquilino(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RespuestaInquilino(_message.Message):
    __slots__ = ["inquilino", "mensaje"]
    INQUILINO_FIELD_NUMBER: _ClassVar[int]
    MENSAJE_FIELD_NUMBER: _ClassVar[int]
    inquilino: Inquilino
    mensaje: str
    def __init__(self, mensaje: _Optional[str] = ..., inquilino: _Optional[_Union[Inquilino, _Mapping]] = ...) -> None: ...
