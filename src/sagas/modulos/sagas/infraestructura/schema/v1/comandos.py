import uuid
from pulsar.schema import *
from dataclasses import dataclass, field
from sagas.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from sagas.seedwork.infraestructura.utils import time_millis

class ComandoCrearSagaPayload(Record):
    fecha_creacion = String()
    fecha_actualizacion = String()
    id = String()
    id_inquilino=String()
    id_propiedad=String()
    dataInquilino=String()
    dataPropiedad=String()

    # TODO Cree los records para itinerarios

class ComandoCrearSaga(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ComandoCrearSagaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ComandoCrearPropiedadPayload(Record):
    fecha_creacion= String()
    fecha_actualizacion= String()
    id= String()
    nombre= String()
    descripcion= String()
    id_cor= String()
    num_habitaciones= Integer()
    num_banos= Integer()
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