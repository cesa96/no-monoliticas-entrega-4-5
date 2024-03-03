from pydispatch import dispatcher

from .handlers import HandlerClienteIntegracion

from clientes.modulos.clientes.dominio.eventos import ClienteCreado

dispatcher.connect(HandlerClienteIntegracion.handle_cliente_creado, signal=f'{ClienteCreado.__name__}Integracion')