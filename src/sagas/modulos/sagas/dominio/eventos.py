from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from sagas.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class SagaCreado(EventoDominio):
    id_saga: uuid.UUID = None
    fecha_creacion: datetime = None
    
