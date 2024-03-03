import clientes.seedwork.presentacion.api as api
import json
from clientes.modulos.clientes.aplicacion.servicios import ServicioCliente
from clientes.modulos.clientes.aplicacion.dto import ClienteDTO
from clientes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from clientes.modulos.clientes.aplicacion.mapeadores import MapeadorClienteDTOJson
from clientes.modulos.clientes.aplicacion.comandos.crear_cliente import CrearCliente
from clientes.modulos.clientes.aplicacion.queries.obtener_cliente import ObtenerCliente
from clientes.modulos.clientes.aplicacion.queries.obtener_todos_cliente import ObtenerTodosCliente
from clientes.seedwork.aplicacion.comandos import ejecutar_commando
from clientes.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('clientes', '/clientes')

@bp.route('/clientes', methods=('POST',))
def clientes_asincrona():
    try:
        cliente_dict = request.json

        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        comando = CrearCliente(cliente_dto.fecha_creacion,
            cliente_dto.fecha_actualizacion,
            cliente_dto.id,
            cliente_dto.nombres,
            cliente_dto.apellidos,
            cliente_dto.identificacion,
            cliente_dto.fecha_nacimiento,
            cliente_dto.genero,
            cliente_dto.direccion,
            cliente_dto.telefono,
            cliente_dto.correo,
            cliente_dto.tipoCliente,
            cliente_dto.sitioWeb)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=201, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/clientes/<id>', methods=('GET',))
def dar_cliente_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerCliente(id))
        map_cliente = MapeadorClienteDTOJson()
        
        return map_cliente.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
    

@bp.route('clientes', methods=('GET',))
def dar_clientes_usando_query():
        query_resultado = ejecutar_query(ObtenerTodosCliente('prueba'))
        map_cliente = MapeadorClienteDTOJson()
        return [map_cliente.dto_a_externo(i) for i in query_resultado]