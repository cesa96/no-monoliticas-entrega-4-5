"""Entidades del dominio de clientes

En este archivo usted encontrará las entidades del dominio de clientes

"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime
import uuid

import clientes.modulos.clientes.dominio.objetos_valor as ov
from clientes.modulos.clientes.dominio.eventos import ClienteCreado
from clientes.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from clientes.seedwork.dominio.objetos_valor import DatoContacto, ObjetoValor, Codigo, Direccion, TipoContacto


@dataclass
class Cliente(AgregacionRaiz):
    nombres: str = field(default=None)
    apellidos: str = field(default=None)
    identificacion: str = field(default=None)
    fecha_nacimiento: datetime = field(default=None)
    genero: ov.Genero = field(default=ov.Genero.MALE)
    direccion: Direccion = field(default=None)
    telefono: DatoContacto = field(default=None)
    correo: DatoContacto = field(default=None)
    tipoCliente: ov.TipoCliente = field(default=ov.TipoCliente.INVERSION)
    sitioWeb: str = field(default=None)

    def crear_cliente(self, cliente: Cliente):
        self.nombres= cliente.nombres
        self.apellidos= cliente.apellidos
        self.identificacion= cliente.identificacion
        self.fecha_nacimiento= cliente.fecha_nacimiento
        self.genero= cliente.genero
        self.direccion= cliente.direccion
        self.telefono= cliente.telefono
        self.correo= cliente.correo
        self.tipoCliente= cliente.tipoCliente
        self.sitioWeb= cliente.sitioWeb
        self.fecha_creacion = datetime.datetime.now()
        self.limpiar_eventos()
        self.agregar_evento(ClienteCreado(id_cliente=self.id,fecha_creacion=self.fecha_creacion))

