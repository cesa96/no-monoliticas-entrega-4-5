""" Fábricas para la creación de objetos del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de propiedades

"""

from .entidades import Propiedad, Propiedad
from .excepciones import TipoObjetoNoExisteEnDominiopropiedadesExcepcion
from propiedades.seedwork.dominio.repositorios import Mapeador, Repositorio
from propiedades.seedwork.dominio.fabricas import Fabrica
from propiedades.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)

            #self.validar_regla(MinimoUnItinerario(propiedad.itinerarios))
            #[self.validar_regla(RutaValida(ruta)) for itin in propiedad.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return propiedad

@dataclass
class Fabricapropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_propiedad = _FabricaPropiedad()
            return fabrica_propiedad.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominiopropiedadesExcepcion()

