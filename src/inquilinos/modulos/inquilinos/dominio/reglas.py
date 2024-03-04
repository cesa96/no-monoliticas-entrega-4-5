"""Reglas de negocio del dominio de inquilino

En este archivo usted encontrará reglas de negocio del dominio de inquilino

"""

from inquilinos.seedwork.dominio.reglas import ReglaNegocio



class TieneNombre(ReglaNegocio):

    nombre: str
    apellido: str

    def __init__(self, nombre, apellido, mensaje='El inquilino debe tener nombre y apellico'):
        super().__init__(mensaje)
        self.nombre = nombre
        self.apellido = apellido

    def es_valido(self) -> bool:
        if self.nombre != None and self.apellido != None:
            return True
        return False
