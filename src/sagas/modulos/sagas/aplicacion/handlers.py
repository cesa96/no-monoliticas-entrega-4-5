from sagas.modulos.sagas.dominio.eventos import SagaCreado
from sagas.seedwork.aplicacion.handlers import Handler
from sagas.modulos.sagas.infraestructura.despachadores import Despachador

class HandlerSagaIntegracion(Handler):

    @staticmethod
    def handle_saga_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-saga')



    