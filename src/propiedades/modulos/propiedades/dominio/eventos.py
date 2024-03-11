from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from propiedades.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class PropiedadCreado(EventoDominio):
    id_propiedad: uuid.UUID = None
    fecha_creacion: datetime = None
    id_cor: str = None
    
@dataclass
class PropiedadEliminada(EventoDominio):
    id_propiedad: uuid.UUID = None
    fecha_eliminacion: datetime = None
    id_cor: str = None
    
@dataclass
class PropiedadCreadoFallo(EventoDominio):
    fecha_creacion: datetime = None
    id_cor: str = None
