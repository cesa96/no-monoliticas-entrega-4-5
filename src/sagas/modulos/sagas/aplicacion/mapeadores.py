import json
from sagas.seedwork.aplicacion.dto import Mapeador as AppMap
from sagas.seedwork.dominio.objetos_valor import DatoContacto, Direccion, TipoContacto
from sagas.seedwork.dominio.repositorios import Mapeador as RepMap
from sagas.modulos.sagas.dominio.entidades import Saga

from .dto import SagaDTO

from datetime import datetime



class MapeadorSagaDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> SagaDTO:


        dataInquilino = json.dumps(externo.get('dataInquilino'))
        dataPropiedad = json.dumps(externo.get('dataPropiedad'))
        saga_dto = SagaDTO(
                    id_inquilino=externo.get('id_inquilino'),
                    id_propiedad=externo.get('id_propiedad'),
                    dataInquilino=dataInquilino,
                    dataPropiedad=dataPropiedad)

        return saga_dto




    def dto_a_externo(self, dto: SagaDTO) -> dict:
        return dto.__dict__


class MapeadorSaga(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def obtener_tipo(self) -> type:
        return Saga.__class__

        

    def entidad_a_dto(self, entidad: Saga) -> SagaDTO:
        
        saga_dto = SagaDTO(fecha_creacion = entidad.fecha_creacion,
                fecha_actualizacion = entidad.fecha_actualizacion,
                id = entidad.id,
                id_inquilino= entidad.id_inquilino,
                id_propiedad= entidad.id_propiedad,
                dataInquilino= entidad.dataInquilino,
                dataPropiedad= entidad.dataPropiedad,
                )


        return saga_dto

    def dto_a_entidad(self, dto: SagaDTO) -> Saga:
        saga = Saga()
        saga = Saga(id=dto.id, 
                    id_inquilino= dto.id_inquilino,
                    id_propiedad= dto.id_propiedad,
                    dataInquilino= dto.dataInquilino,
                    dataPropiedad= dto.dataPropiedad,                   
                    )


        return saga



