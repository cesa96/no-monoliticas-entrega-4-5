from dataclasses import dataclass, field
from sagas.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class SagaDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    id_inquilino: str = field(default_factory=str)
    id_propiedad: str = field(default_factory=str)
    dataInquilino: str = field(default_factory=str)
    dataPropiedad: str = field(default_factory=str)
