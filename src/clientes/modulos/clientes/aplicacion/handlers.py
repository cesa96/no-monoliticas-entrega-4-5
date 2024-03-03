from clientes.modulos.clientes.dominio.eventos import ClienteCreado
from clientes.seedwork.aplicacion.handlers import Handler
from clientes.modulos.clientes.infraestructura.despachadores import Despachador

class HandlerClienteIntegracion(Handler):

    @staticmethod
    def handle_cliente_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')



    