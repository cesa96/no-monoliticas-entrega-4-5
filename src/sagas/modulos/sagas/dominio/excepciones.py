""" Excepciones del dominio de sagas

En este archivo usted encontrará los Excepciones relacionadas
al dominio de sagas

"""

from sagas.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominiosagasExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de sagas'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)