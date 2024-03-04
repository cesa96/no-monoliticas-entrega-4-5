"""Entidades del dominio de inquilinos

En este archivo usted encontrará las entidades del dominio de inquilinos

"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import uuid

import inquilinos.modulos.inquilinos.dominio.objetos_valor as ov
from inquilinos.modulos.inquilinos.dominio.eventos import InquilinoCreado, PropiedadAsociada
from inquilinos.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from inquilinos.seedwork.dominio.objetos_valor import DatoContacto, ObjetoValor, Codigo, Direccion, TipoContacto



@dataclass(frozen=True)
class PropiedadInquilino(ObjetoValor):
    id_propiedad: str = field(default=None)
    #_id: uuid.UUID = field(init=False, repr=False, hash=True)
    fecha_creacion: str =  field(default=datetime.now().isoformat())
    fecha_actualizacion: str = field(default=datetime.now().isoformat())
    id: uuid.UUID = field(default=None,hash=True)
#     @classmethod
#     def siguiente_id(self) -> uuid.UUID:
#         return uuid.uuid4()

#     @property
#     def id(self):
#         return self._id

#     @id.setter
#     def id(self, id: uuid.UUID) -> None:
# #        if not IdEntidadEsInmutable(self).es_valido():
# #            raise IdDebeSerInmutableExcepcion()
#         if id:
#             self._id = id
#         else:
#             self._id = self.siguiente_id()

@dataclass
class Inquilino(AgregacionRaiz):
    nombres: str = field(default=None)
    apellidos: str = field(default=None)
    identificacion: str = field(default=None)
    fecha_nacimiento: datetime = field(default=None)
    genero: ov.Genero = field(default=ov.Genero.MALE)
    direccion: Direccion = field(default=None)
    telefono: DatoContacto = field(default=None)
    correo: DatoContacto = field(default=None)
    sitioWeb: str = field(default=None)
    propiedades: list[PropiedadInquilino]= field(default_factory=list[PropiedadInquilino])

    def crear_inquilino(self, inquilino: Inquilino):
        self.nombres= inquilino.nombres
        self.apellidos= inquilino.apellidos
        self.identificacion= inquilino.identificacion
        self.fecha_nacimiento= inquilino.fecha_nacimiento
        self.genero= inquilino.genero
        self.direccion= inquilino.direccion
        self.telefono= inquilino.telefono
        self.correo= inquilino.correo
        self.sitioWeb= inquilino.sitioWeb
        self.fecha_creacion = datetime.now()
        self.limpiar_eventos()
        self.agregar_evento(InquilinoCreado(id_inquilino=self.id,fecha_creacion=self.fecha_creacion))

    def asociar_propiedad(self, id_propiedad:str):
        propiedadInquilino:  PropiedadInquilino = PropiedadInquilino(id=uuid.uuid4(),id_propiedad=id_propiedad)
        self.propiedades.append(propiedadInquilino)
        self.limpiar_eventos()
        self.agregar_evento(PropiedadAsociada(id_inquilino=self.id, id_propiedad=id_propiedad, id=propiedadInquilino.id, fecha_creacion=datetime.now()))


