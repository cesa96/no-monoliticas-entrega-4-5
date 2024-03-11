import uuid
from pulsar.schema import *
from dataclasses import dataclass, field
from inquilinos.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from inquilinos.seedwork.infraestructura.utils import time_millis

class ComandoCrearInquilinoPayload(Record):
    fecha_creacion= String()
    fecha_actualizacion= String()
    id= String()
    nombres= String()
    apellidos= String()
    identificacion= String()
    fecha_nacimiento= String()
    genero= String()
    id_cor= String()
    direccion= String()
    telefono= String()
    correo= String()
    sitioWeb= String()


class ComandoCrearInquilino(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ComandoCrearInquilinoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoAsociarPropiedadPayload(Record):
    id_inquilino= String()
    id_propiedad= String()
    id_cor=String()



class ComandoAsociarPropiedad(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ComandoAsociarPropiedadPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoEliminarInquilinoPayload(Record):
    id_inquilino= String()
    id_cor=String()



class ComandoEliminarInquilino(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ComandoEliminarInquilinoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)