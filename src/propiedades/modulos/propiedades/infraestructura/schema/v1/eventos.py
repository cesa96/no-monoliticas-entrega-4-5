import uuid
from pulsar.schema import *
from propiedades.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from propiedades.seedwork.infraestructura.utils import time_millis

class PropiedadCreadoPayload(Record):
    id_propiedad = String()
    id_cor = String()
    fecha_creacion = Long()

class EventoPropiedadCreado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = PropiedadCreadoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PropiedadCreadoFalloPayload(Record):
    id_cor = String()
    fecha_creacion = Long()

class EventoPropiedadCreadoFallo(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = PropiedadCreadoFalloPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
