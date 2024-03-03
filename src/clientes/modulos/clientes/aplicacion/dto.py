from dataclasses import dataclass, field
from clientes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class ClienteDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombres: str = field(default_factory=str)
    apellidos: str = field(default_factory=str)
    identificacion: str = field(default_factory=str)
    fecha_nacimiento: str = field(default_factory=str)
    genero: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    telefono: str = field(default_factory=str)
    correo: str = field(default_factory=str)
    tipoCliente: str = field(default_factory=str)
    sitioWeb: str = field(default_factory=str)
