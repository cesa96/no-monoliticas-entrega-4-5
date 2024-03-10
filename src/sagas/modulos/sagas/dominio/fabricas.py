""" Fábricas para la creación de objetos del dominio de sagas

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de sagas

"""

from .entidades import Saga, Saga
from .excepciones import TipoObjetoNoExisteEnDominiosagasExcepcion
from sagas.seedwork.dominio.repositorios import Mapeador, Repositorio
from sagas.seedwork.dominio.fabricas import Fabrica
from sagas.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaSaga(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            saga: Saga = mapeador.dto_a_entidad(obj)

            #self.validar_regla(MinimoUnItinerario(saga.itinerarios))
            #[self.validar_regla(RutaValida(ruta)) for itin in saga.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return saga

@dataclass
class Fabricasagas(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Saga.__class__:
            fabrica_saga = _FabricaSaga()
            return fabrica_saga.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominiosagasExcepcion()

