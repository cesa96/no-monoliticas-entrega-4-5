"""Reglas de negocio del dominio de propiedad

En este archivo usted encontrará reglas de negocio del dominio de propiedad

"""

from propiedades.seedwork.dominio.reglas import ReglaNegocio



class TieneNombre(ReglaNegocio):

    nombre: str

    def __init__(self, nombre, mensaje='El propiedad debe tener nombre y apellico'):
        super().__init__(mensaje)
        self.nombre = nombre

    def es_valido(self) -> bool:
        if self.nombre != None:
            return True
        return False
