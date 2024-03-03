import uuid
from pulsar.schema import *
from clientes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from clientes.seedwork.infraestructura.utils import time_millis

class ClienteCreadoPayload(Record):
    id_cliente = String()
    fecha_creacion = Long()

class EventoClienteCreado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ClienteCreadoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)