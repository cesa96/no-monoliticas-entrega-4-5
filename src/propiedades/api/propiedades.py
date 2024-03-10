from propiedades.modulos.propiedades.infraestructura.despachadores import Despachador
import propiedades.seedwork.presentacion.api as api
import json
from propiedades.modulos.propiedades.aplicacion.servicios import ServicioPropiedad
from propiedades.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedades.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from propiedades.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from propiedades.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedades.modulos.propiedades.aplicacion.queries.obtener_propiedad import ObtenerPropiedad
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando
from propiedades.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('propiedades', '/propiedades')

@bp.route('/propiedades', methods=('POST',))
def propiedades_asincrona():
    try:
        propiedad_dict = request.json

        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)


        comando = CrearPropiedad(propiedad_dto.fecha_creacion,
            propiedad_dto.fecha_actualizacion,
            propiedad_dto.id,
            propiedad_dto.nombre,
            propiedad_dto.descripcion,
            propiedad_dto.num_habitaciones,
            propiedad_dto.id_cor,
            propiedad_dto.num_banos,
            propiedad_dto.fecha_construccion,
            propiedad_dto.fecha_modernizacion,
            propiedad_dto.disponible,
            propiedad_dto.direccion,
            propiedad_dto.precio,
            propiedad_dto.metrosCuadrados, propiedad_dto.tipoPropiedad, propiedad_dto.servicios)

        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos2-propiedad')


        
        return Response('{}', status=201, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/propiedades/<id>', methods=('GET',))
def dar_propiedad_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerPropiedad(id))
        map_propiedad = MapeadorPropiedadDTOJson()
        
        return map_propiedad.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
    