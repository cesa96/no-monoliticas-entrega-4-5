import uuid
from pulsar.schema import *
from dataclasses import dataclass, field
from clientes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from clientes.seedwork.infraestructura.utils import time_millis

class ComandoCrearClientePayload(Record):
    fecha_creacion = String()
    fecha_actualizacion = String()
    id = String()
    nombres = String()
    apellidos = String()
    identificacion = String()
    fecha_nacimiento = String()
    genero = String()
    direccion = String()
    telefono = String()
    correo = String()
    tipoCliente = String()
    sitioWeb = String()

    # TODO Cree los records para itinerarios

class ComandoCrearCliente(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ComandoCrearClientePayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

