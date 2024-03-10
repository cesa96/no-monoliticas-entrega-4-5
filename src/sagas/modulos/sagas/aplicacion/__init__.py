from pydispatch import dispatcher

from .handlers import HandlerSagaIntegracion

from sagas.modulos.sagas.dominio.eventos import SagaCreado

dispatcher.connect(HandlerSagaIntegracion.handle_saga_creado, signal=f'{SagaCreado.__name__}Integracion')