"""Entidades del dominio de propiedades

En este archivo usted encontrará las entidades del dominio de propiedades

"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime
import uuid

import propiedades.modulos.propiedades.dominio.objetos_valor as ov
from propiedades.modulos.propiedades.dominio.eventos import PropiedadCreado
from propiedades.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from propiedades.seedwork.dominio.objetos_valor import float, ObjetoValor, Codigo, Direccion, TipoContacto


@dataclass
class Propiedad(AgregacionRaiz):
    nombre: str = field(default=None)
    descripcion: str = field(default=None)
    id_cor: str = field(default=None)
    num_habitaciones: int = field(default=None)
    num_banos: int = field(default=None)
    fecha_construccion: datetime = field(default=None)
    fecha_modernizacion: datetime = field(default=None)
    disponible: bool = field(default=True)
    direccion: Direccion = field(default=None)
    precio: float = field(default=None)
    metrosCuadrados: float = field(default=None)
    tipoPropiedad: ov.TipoPropiedad = field(default=ov.TipoPropiedad.CASA)
    servicios: str = field(default=None)

    def crear_propiedad(self, propiedad: Propiedad):
        self.nombre= propiedad.nombre
        self.descripcion= propiedad.descripcion
        self.id_cor= propiedad.id_cor
        self.num_habitaciones= propiedad.num_habitaciones
        self.num_banos= propiedad.num_banos
        self.fecha_construccion= propiedad.fecha_construccion
        self.fecha_modernizacion= propiedad.fecha_construccion
        self.disponible= propiedad.disponible
        self.direccion= propiedad.direccion
        self.precio= propiedad.precio
        self.metrosCuadrados= propiedad.metrosCuadrados
        self.tipoPropiedad= propiedad.tipoPropiedad
        self.servicios= propiedad.servicios
        self.fecha_creacion = datetime.datetime.now()
        self.limpiar_eventos()
        self.agregar_evento(PropiedadCreado(id_propiedad=self.id,id_cor=self.id_cor,fecha_creacion=self.fecha_creacion))

