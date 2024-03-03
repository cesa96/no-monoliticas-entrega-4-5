"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from clientes.seedwork.dominio.reglas import ReglaNegocio



class TieneNombre(ReglaNegocio):

    nombre: str
    apellido: str

    def __init__(self, nombre, apellido, mensaje='El cliente debe tener nombre y apellico'):
        super().__init__(mensaje)
        self.nombre = nombre
        self.apellido = apellido

    def es_valido(self) -> bool:
        if self.nombre != None and self.apellido != None:
            return True
        return False
