""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de propiedades

"""

from propiedades.config.db import db
from propiedades.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedades.modulos.propiedades.dominio.entidades import  Propiedad
from propiedades.modulos.propiedades.dominio.fabricas import Fabricapropiedades
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad
from uuid import UUID



class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedades: Fabricapropiedades = Fabricapropiedades()

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)

    def actualizar(self, propiedad: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        propiedad_dto:PropiedadDTO = db.session.query(PropiedadDTO).filter_by(id=str(propiedad_id)).one()
        db.session.delete(propiedad_dto)
        raise NotImplementedError