from dataclasses import dataclass, field
from inquilinos.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropiedadesInquilinoDTO(DTO):
    id: str = field(default_factory=str)
    id_propiedad: str = field(default_factory=str)
    id_inquilino: str = field(default_factory=str)


@dataclass(frozen=True)
class InquilinoDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombres: str = field(default_factory=str)
    apellidos: str = field(default_factory=str)
    identificacion: str = field(default_factory=str)
    fecha_nacimiento: str = field(default_factory=str)
    genero: str = field(default_factory=str)
    id_cor: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    telefono: str = field(default_factory=str)
    correo: str = field(default_factory=str)
    sitioWeb: str = field(default_factory=str)
    propiedades: list[PropiedadesInquilinoDTO]   = field(default_factory=list)
