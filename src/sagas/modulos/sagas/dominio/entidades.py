"""Entidades del dominio de sagas

En este archivo usted encontrará las entidades del dominio de sagas

"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime
import uuid

import sagas.modulos.sagas.dominio.objetos_valor as ov
from sagas.modulos.sagas.dominio.eventos import SagaCreado
from sagas.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from sagas.seedwork.dominio.objetos_valor import DatoContacto, ObjetoValor, Codigo, Direccion, TipoContacto


@dataclass
class Saga(AgregacionRaiz):
    id_inquilino: str = field(default=None)
    id_propiedad: str = field(default=None)
    dataInquilino: str = field(default=None)
    dataPropiedad: str = field(default=None)


    def crear_saga(self, saga: Saga):
        self.id_inquilino= saga.id_inquilino
        self.id_propiedad= saga.id_propiedad
        self.dataInquilino= saga.dataInquilino
        self.dataPropiedad= saga.dataPropiedad
        self.fecha_creacion = datetime.datetime.now()
        self.limpiar_eventos()
        self.agregar_evento(SagaCreado(id_saga=self.id,fecha_creacion=self.fecha_creacion))

