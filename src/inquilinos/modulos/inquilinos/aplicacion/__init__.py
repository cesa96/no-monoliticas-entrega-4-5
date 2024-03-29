from pydispatch import dispatcher

from .handlers import HandlerInquilinoIntegracion

from inquilinos.modulos.inquilinos.dominio.eventos import InquilinoCreado, PropiedadAsociada, InquilinoEliminado

dispatcher.connect(HandlerInquilinoIntegracion.handle_inquilino_creado, signal=f'{InquilinoCreado.__name__}Integracion')
dispatcher.connect(HandlerInquilinoIntegracion.handle_propiedad_asociada, signal=f'{PropiedadAsociada.__name__}Integracion')
dispatcher.connect(HandlerInquilinoIntegracion.handle_inquilino_eliminado, signal=f'{InquilinoEliminado.__name__}Integracion')