from clientes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from clientes.seedwork.aplicacion.queries import ejecutar_query as query
from clientes.modulos.clientes.infraestructura.repositorios import RepositorioClientes
from dataclasses import dataclass
from .base import ClienteQueryBaseHandler
from clientes.modulos.clientes.aplicacion.mapeadores import MapeadorCliente
import uuid

@dataclass
class ObtenerCliente(Query):
    id: str

class ObtenerClienteHandler(ClienteQueryBaseHandler):

    def handle(self, query: ObtenerCliente) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)
        cliente =  self.fabrica_clientes.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorCliente())
        return QueryResultado(resultado=cliente)

@query.register(ObtenerCliente)
def ejecutar_query_obtener_cliente(query: ObtenerCliente):
    handler = ObtenerClienteHandler()
    return handler.handle(query)