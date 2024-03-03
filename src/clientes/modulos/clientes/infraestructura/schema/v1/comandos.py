from pulsar.schema import *
from dataclasses import dataclass, field
from clientes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearClientePayload(Record):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearCliente(ComandoIntegracion):
    data = ComandoCrearClientePayload()