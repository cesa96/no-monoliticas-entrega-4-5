"""Entidades reusables parte del seedwork del proyecto

En este archivo usted encontrará las entidades reusables parte del seedwork del proyecto

"""

from dataclasses import dataclass, field
from .eventos import EventoDominio
from .mixins import ValidarReglasMixin
from .reglas import IdEntidadEsInmutable
from .excepciones import IdDebeSerInmutableExcepcion
from datetime import datetime
import uuid

@dataclass
class Entidad:
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    fecha_creacion: str =  field(default=datetime.now().isoformat())
    fecha_actualizacion: str = field(default=datetime.now().isoformat())

    @classmethod
    def siguiente_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
#        if not IdEntidadEsInmutable(self).es_valido():
#            raise IdDebeSerInmutableExcepcion()
        if id:
            self._id = id
        else:
            self._id = self.siguiente_id()
        

@dataclass
class AgregacionRaiz(Entidad, ValidarReglasMixin):
    eventos: list[EventoDominio] = field(default_factory=list)
    def __init__(self):
        self.eventos = list()

    def agregar_evento(self, evento: EventoDominio):
        self.eventos = list()
        self.eventos.append(evento)
    
    def limpiar_eventos(self):
        self.eventos = list()
        