""" Interfaces para los repositorios del dominio de sagas

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de sagas

"""

from abc import ABC
from sagas.seedwork.dominio.repositorios import Repositorio

class RepositorioSagas(Repositorio, ABC):
    ...
