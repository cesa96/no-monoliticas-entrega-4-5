from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from inquilinos.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class InquilinoCreado(EventoDominio):
    id_inquilino: uuid.UUID = None
    fecha_creacion: datetime = None
    id_cor: str = None
    

@dataclass
class PropiedadAsociada(EventoDominio):
    id_inquilino: uuid.UUID = None
    id_propiedad: uuid.UUID = None
    id: uuid.UUID = None
    fecha_creacion: datetime = None
    id_cor: str = None

@dataclass
class InquilinoEliminado(EventoDominio):
    id_inquilino: uuid.UUID = None
    fecha_eliminacion: datetime = None
    id_cor: str = None
    
@dataclass
class InquilinoCreadoFallo(EventoDominio):
    fecha_creacion: datetime = None
    id_cor: str = None
    