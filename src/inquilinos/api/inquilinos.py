from inquilinos.modulos.inquilinos.aplicacion.comandos.asociar_propiedad import AsociarPropiedad
import inquilinos.seedwork.presentacion.api as api
import json
from inquilinos.modulos.inquilinos.aplicacion.servicios import ServicioInquilino
from inquilinos.modulos.inquilinos.aplicacion.dto import InquilinoDTO
from inquilinos.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from inquilinos.modulos.inquilinos.aplicacion.mapeadores import MapeadorInquilinoDTOJson
from inquilinos.modulos.inquilinos.aplicacion.comandos.crear_inquilino import CrearInquilino
from inquilinos.modulos.inquilinos.aplicacion.queries.obtener_inquilino import ObtenerInquilino
from inquilinos.seedwork.aplicacion.comandos import ejecutar_commando
from inquilinos.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('inquilinos', '/inquilinos')

@bp.route('/inquilinos', methods=('POST',))
def inquilinos_asincrona():
    try:
        inquilino_dict = request.json

        map_inquilino = MapeadorInquilinoDTOJson()
        inquilino_dto = map_inquilino.externo_a_dto(inquilino_dict)

        comando = CrearInquilino(inquilino_dto.fecha_creacion,
            inquilino_dto.fecha_actualizacion,
            inquilino_dto.id,
            inquilino_dto.nombres,
            inquilino_dto.apellidos,
            inquilino_dto.identificacion,
            inquilino_dto.fecha_nacimiento,
            inquilino_dto.genero,
            inquilino_dto.direccion,
            inquilino_dto.telefono,
            inquilino_dto.correo,
            inquilino_dto.sitioWeb)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=201, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/inquilinos/<id>/asociar_propiedad/<id_propiedad>', methods=('PUT',))
def asociar_propiedad(id=None, id_propiedad=None):
    try:

        comando = AsociarPropiedad(id_inquilino=id, id_propiedad=id_propiedad)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=200, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/inquilinos/<id>', methods=('GET',))
def dar_inquilino_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerInquilino(id))
        map_inquilino = MapeadorInquilinoDTOJson()
        
        return map_inquilino.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
