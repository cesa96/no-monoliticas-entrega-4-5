import datetime
from sagas.modulos.sagas.dominio.objetos_valor import Genero, TipoSaga
from sagas.seedwork.aplicacion.comandos import Comando
from sagas.modulos.sagas.aplicacion.dto import SagaDTO
from sagas.seedwork.dominio.objetos_valor import Direccion, TipoContacto
from .base import CrearSagaBaseHandler
from dataclasses import dataclass, field
from sagas.seedwork.aplicacion.comandos import ejecutar_commando as comando

from sagas.modulos.sagas.dominio.entidades import Saga
from sagas.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from sagas.modulos.sagas.aplicacion.mapeadores import MapeadorSaga
from sagas.modulos.sagas.infraestructura.repositorios import RepositorioSagas

@dataclass
class CrearSaga(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    id_inquilino: str 
    id_propiedad: str 
    dataInquilino: str 
    dataPropiedad: str 


class CrearSagaHandler(CrearSagaBaseHandler):
    
    def handle(self, comando: CrearSaga):
        saga_dto = SagaDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   id_inquilino=comando.id_inquilino
            ,   id_propiedad=comando.id_propiedad
            ,   dataInquilino=comando.dataInquilino
            ,   dataPropiedad=comando.dataPropiedad
            
            
            
            )

        saga: Saga = self.fabrica_sagas.crear_objeto(saga_dto, MapeadorSaga())
        saga.crear_saga(saga)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSagas.__class__)
        UnidadTrabajoPuerto.limpiar()
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, saga)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearSaga)
def ejecutar_comando_crear_saga(comando: CrearSaga):
    handler = CrearSagaHandler()
    handler.handle(comando)
    