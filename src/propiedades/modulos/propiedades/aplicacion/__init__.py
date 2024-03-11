from pydispatch import dispatcher

from .handlers import HandlerPropiedadIntegracion

from propiedades.modulos.propiedades.dominio.eventos import PropiedadCreado, PropiedadEliminada

dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_creado, signal=f'{PropiedadCreado.__name__}Integracion')
dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_eliminada, signal=f'{PropiedadEliminada.__name__}Integracion')