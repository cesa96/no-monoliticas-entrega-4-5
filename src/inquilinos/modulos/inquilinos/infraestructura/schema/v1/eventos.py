import uuid
from pulsar.schema import *
from inquilinos.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from inquilinos.seedwork.infraestructura.utils import time_millis

class InquilinoCreadoPayload(Record):
    id_inquilino = String()
    fecha_creacion = Long()

class EventoInquilinoCreado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = InquilinoCreadoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)