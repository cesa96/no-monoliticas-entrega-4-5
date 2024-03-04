from dataclasses import dataclass, field
from propiedades.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class PropiedadDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    num_habitaciones: int = field(default_factory=int)
    num_banos: int = field(default_factory=int)
    fecha_construccion: str = field(default_factory=str)
    fecha_modernizacion: str = field(default_factory=str)
    disponible: bool = field(default_factory=bool)
    direccion: str = field(default_factory=str)
    precio: float = field(default_factory=float)
    metrosCuadrados: float = field(default_factory=float)
    tipoPropiedad: str = field(default_factory=str)
    servicios: str = field(default_factory=str)
