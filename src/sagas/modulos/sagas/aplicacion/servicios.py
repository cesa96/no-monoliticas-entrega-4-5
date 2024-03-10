from sagas.seedwork.aplicacion.servicios import Servicio
from sagas.modulos.sagas.dominio.entidades import Saga
from sagas.modulos.sagas.dominio.fabricas import Fabricasagas
from sagas.modulos.sagas.infraestructura.fabricas import FabricaRepositorio
from sagas.modulos.sagas.infraestructura.repositorios import RepositorioSagas
from sagas.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorSaga

from .dto import SagaDTO

import asyncio

class ServicioSaga(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_sagas: Fabricasagas = Fabricasagas()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_sagas(self):
        return self._fabrica_sagas       
    
    def crear_saga(self, saga_dto: SagaDTO) -> SagaDTO:
        saga: Saga = self.fabrica_sagas.crear_objeto(saga_dto, MapeadorSaga())
        saga.crear_saga(saga)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSagas.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, saga)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_sagas.crear_objeto(saga, MapeadorSaga())

    def obtener_saga_por_id(self, id) -> SagaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSagas.__class__)
        return self.fabrica_sagas.crear_objeto(repositorio.obtener_por_id(id), MapeadorSaga())


    def obtener_sagas(self, id) -> SagaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSagas.__class__)
        return self.fabrica_sagas.crear_objeto(repositorio.obtener_por_id(id), MapeadorSaga())
