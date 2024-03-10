import uuid
from pulsar.schema import *
from sagas.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from sagas.seedwork.infraestructura.utils import time_millis

class SagaCreadoPayload(Record):
    id_saga = String()
    fecha_creacion = Long()

class EventoSagaCreado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = SagaCreadoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class InquilinoCreadoPayload(Record):
    id_inquilino = String()
    id_cor = String()
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

class PropiedadAsociadaPayload(Record):
    id_inquilino = String()
    id_propiedad = String()
    id_cor = String()

class EventoPropiedadAsociada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = PropiedadAsociadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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