""" Fábricas para la creación de objetos del dominio de inquilinos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de inquilinos

"""

from .entidades import Inquilino, Inquilino
from .excepciones import TipoObjetoNoExisteEnDominioinquilinosExcepcion
from inquilinos.seedwork.dominio.repositorios import Mapeador, Repositorio
from inquilinos.seedwork.dominio.fabricas import Fabrica
from inquilinos.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaInquilino(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            inquilino: Inquilino = mapeador.dto_a_entidad(obj)

            #self.validar_regla(MinimoUnItinerario(inquilino.itinerarios))
            #[self.validar_regla(RutaValida(ruta)) for itin in inquilino.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return inquilino

@dataclass
class Fabricainquilinos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Inquilino.__class__:
            fabrica_inquilino = _FabricaInquilino()
            return fabrica_inquilino.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioinquilinosExcepcion()

