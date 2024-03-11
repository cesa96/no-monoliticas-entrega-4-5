""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de inquilinos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de inquilinos

"""

from inquilinos.config.db import db
from inquilinos.modulos.inquilinos.dominio.repositorios import RepositorioInquilinos
from inquilinos.modulos.inquilinos.dominio.entidades import  Inquilino
from inquilinos.modulos.inquilinos.dominio.fabricas import Fabricainquilinos
from .dto import Inquilino as InquilinoDTO, PropiedadesInquilino
from .mapeadores import MapeadorInquilino
from uuid import UUID



class RepositorioInquilinosSQLite(RepositorioInquilinos):

    def __init__(self):
        self._fabrica_inquilinos: Fabricainquilinos = Fabricainquilinos()

    @property
    def fabrica_inquilinos(self):
        return self._fabrica_inquilinos

    def obtener_por_id(self, id: UUID) -> Inquilino:
        inquilino_dto = db.session.query(InquilinoDTO).filter_by(id=str(id)).one()
        return self.fabrica_inquilinos.crear_objeto(inquilino_dto, MapeadorInquilino())

    def obtener_todos(self) -> list[Inquilino]:
        # TODO
        raise NotImplementedError

    def agregar(self, inquilino: Inquilino):
        inquilino_dto = self.fabrica_inquilinos.crear_objeto(inquilino, MapeadorInquilino())
        db.session.add(inquilino_dto)

    def actualizar(self, inquilino: Inquilino):
        inquilino_dto1: InquilinoDTO = self.fabrica_inquilinos.crear_objeto(inquilino, MapeadorInquilino())
        print(f'Id inquilino: {str(inquilino.id)}')
        inquilino_dto2:InquilinoDTO = db.session.query(InquilinoDTO).filter_by(id=str(inquilino.id)).one()
        inquilino_dto2.nombres = "Cesar prueba"
        for prop1 in inquilino_dto1.propiedades:
            exists = False
            for prop2 in inquilino_dto2.propiedades:
                if str(prop1.id) == str(prop2.id):
                    exists = True
            if not exists:
                inquilino_dto2.propiedades.append(PropiedadesInquilino(id=prop1.id, id_propiedad=prop1.id_propiedad))

    def eliminar(self, inquilino_id: UUID):
        # TODO
        inquilino_dto:InquilinoDTO = db.session.query(InquilinoDTO).filter_by(id=str(inquilino_id)).one()
        db.session.delete(inquilino_dto)
