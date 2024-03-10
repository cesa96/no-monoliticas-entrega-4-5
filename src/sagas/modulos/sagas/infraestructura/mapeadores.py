""" Mapeadores para la capa de infrastructura del dominio de sagas

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from sagas.seedwork.dominio.repositorios import Mapeador
from sagas.modulos.sagas.dominio.objetos_valor import Genero, TipoSaga
from sagas.modulos.sagas.dominio.entidades import  Saga
from .dto import Saga as SagaDTO
from sagas.seedwork.dominio.objetos_valor import DatoContacto, Direccion, TipoContacto

class MapeadorSaga(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def entidad_a_dto(self, entidad: Saga) -> SagaDTO:
        
        saga_dto = SagaDTO()
        saga_dto.fecha_creacion = entidad.fecha_creacion
        saga_dto.fecha_actualizacion = entidad.fecha_actualizacion
        saga_dto.id = str(entidad.id)
        saga_dto.id_inquilino = str(entidad.id_inquilino)
        saga_dto.id_propiedad = str(entidad.id_propiedad)
        saga_dto.dataInquilino = entidad.dataInquilino
        saga_dto.dataPropiedad = entidad.dataPropiedad


        return saga_dto

    def dto_a_entidad(self, dto: SagaDTO) -> Saga:
        saga = Saga(id=dto.id, 
                    id_inquilino=dto.id_inquilino,
                    id_propiedad=dto.id_propiedad,
                    dataInquilino=dto.dataInquilino,
                    dataPropiedad=dto.dataPropiedad
                    
                    
                    )
        
        return saga
    
    def obtener_tipo(self) -> type:
        return Saga.__class__