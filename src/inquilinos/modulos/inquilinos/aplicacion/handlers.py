from inquilinos.modulos.inquilinos.dominio.eventos import InquilinoCreado
from inquilinos.seedwork.aplicacion.handlers import Handler
from inquilinos.modulos.inquilinos.infraestructura.despachadores import Despachador

class HandlerInquilinoIntegracion(Handler):

    @staticmethod
    def handle_inquilino_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos2-inquilino')

    @staticmethod
    def handle_propiedad_asociada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-asociar-propiedad3')


    