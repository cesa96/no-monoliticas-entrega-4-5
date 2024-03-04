from pulsar.schema import *
from dataclasses import dataclass, field
from propiedades.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearPropiedadPayload(Record):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()