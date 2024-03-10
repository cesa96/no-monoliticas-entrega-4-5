""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de sagas

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de sagas

"""

from sagas.config.db import db
from sagas.modulos.sagas.dominio.repositorios import RepositorioSagas
from sagas.modulos.sagas.dominio.entidades import  Saga
from sagas.modulos.sagas.dominio.fabricas import Fabricasagas
from .dto import Saga as SagaDTO
from .mapeadores import MapeadorSaga
from uuid import UUID



class RepositorioSagasSQLite(RepositorioSagas):

    def __init__(self):
        self._fabrica_sagas: Fabricasagas = Fabricasagas()

    @property
    def fabrica_sagas(self):
        return self._fabrica_sagas

    def obtener_por_id(self, id: UUID) -> Saga:
        saga_dto = db.session.query(SagaDTO).filter_by(id=str(id)).one()
        return self.fabrica_sagas.crear_objeto(saga_dto, MapeadorSaga())

    def obtener_todos(self) -> list[Saga]:
        # TODO
        raise NotImplementedError

    def agregar(self, saga: Saga):
        saga_dto = self.fabrica_sagas.crear_objeto(saga, MapeadorSaga())
        db.session.add(saga_dto)

    def actualizar(self, saga: Saga):
        sagaDto:SagaDTO = db.session.query(SagaDTO).filter_by(id=str(saga.id)).one()
        sagaDto.id_inquilino = saga.id_inquilino
        sagaDto.id_propiedad = saga.id_propiedad

    def eliminar(self, saga_id: UUID):
        # TODO
        raise NotImplementedError