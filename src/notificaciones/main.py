import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os

def time_millis():
    return int(time.time() * 1000)

class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class ClienteCreadaPayload(Record):
    id_cliente = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoClienteCreada(EventoIntegracion):
    data = ClienteCreadaPayload()

HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe('eventos-cliente', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='sub-notificacion-eventos-clientes', schema=AvroSchema(EventoClienteCreada))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value().data)
    print('=========================================')

    print('==== Envía correo a usuario ====')

    consumer.acknowledge(msg)

client.close()