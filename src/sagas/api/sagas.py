from sagas.modulos.sagas.infraestructura.despachadores import Despachador
import sagas.seedwork.presentacion.api as api
import json
from sagas.modulos.sagas.aplicacion.servicios import ServicioSaga
from sagas.modulos.sagas.aplicacion.dto import SagaDTO
from sagas.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from sagas.modulos.sagas.aplicacion.mapeadores import MapeadorSagaDTOJson
from sagas.modulos.sagas.aplicacion.comandos.crear_saga import CrearSaga
from sagas.seedwork.aplicacion.comandos import ejecutar_commando
from sagas.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('sagas', '/sagas')

@bp.route('/sagas', methods=('POST',))
def sagas_asincrona():
    try:
        saga_dict = request.json

        map_saga = MapeadorSagaDTOJson()
        saga_dto = map_saga.externo_a_dto(saga_dict)

        comando = CrearSaga(saga_dto.fecha_creacion,
            saga_dto.fecha_actualizacion,
            saga_dto.id,
            saga_dto.id_inquilino,
            saga_dto.id_propiedad,
            saga_dto.dataInquilino,
            saga_dto.dataPropiedad
            )

        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-saga')

        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        #ejecutar_commando(comando)
        
        return Response('{}', status=201, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
