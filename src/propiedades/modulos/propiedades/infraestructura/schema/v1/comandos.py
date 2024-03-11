import uuid
from pulsar.schema import *
from dataclasses import dataclass, field
from propiedades.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from propiedades.seedwork.infraestructura.utils import time_millis

class ComandoCrearPropiedadPayload(Record):
    fecha_creacion= String()
    fecha_actualizacion= String()
    id= String()
    nombre= String()
    descripcion= String()
    id_cor= String()
    num_habitaciones= Integer()
    num_banos=  Integer()
    fecha_construccion= String()
    fecha_modernizacion= String()
    disponible= Boolean()
    direccion= String()
    precio= Float()
    metrosCuadrados= Float()
    tipoPropiedad= String()
    servicios= String()

class ComandoCrearPropiedad(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ComandoCrearPropiedadPayload()

class ComandoEliminarPropiedadPayload(Record):
    id_inquilino= String()
    id_cor=String()



class ComandoEliminarPropiedad(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ComandoEliminarPropiedadPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)