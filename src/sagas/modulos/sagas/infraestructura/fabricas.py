""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de sagas

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de sagas

"""

from dataclasses import dataclass, field
from sagas.seedwork.dominio.fabricas import Fabrica
from sagas.seedwork.dominio.repositorios import Repositorio
from sagas.modulos.sagas.dominio.repositorios import RepositorioSagas
from .repositorios import RepositorioSagasSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioSagas.__class__:
            return RepositorioSagasSQLite()
        else:
            raise ExcepcionFabrica()