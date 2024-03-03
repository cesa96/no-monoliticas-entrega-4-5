""" Interfaces para los repositorios del dominio de clientes

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de clientes

"""

from abc import ABC
from clientes.seedwork.dominio.repositorios import Repositorio

class RepositorioClientes(Repositorio, ABC):
    ...
