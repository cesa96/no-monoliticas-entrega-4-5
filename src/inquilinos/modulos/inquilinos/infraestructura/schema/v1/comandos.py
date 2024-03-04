from pulsar.schema import *
from dataclasses import dataclass, field
from inquilinos.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearInquilinoPayload(Record):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearInquilino(ComandoIntegracion):
    data = ComandoCrearInquilinoPayload()