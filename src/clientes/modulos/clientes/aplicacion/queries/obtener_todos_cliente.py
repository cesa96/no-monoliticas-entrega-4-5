from dataclasses import dataclass
from clientes.modulos.clientes.aplicacion.dto import ClienteDTO
from clientes.modulos.clientes.aplicacion.mapeadores import MapeadorCliente
from clientes.modulos.clientes.aplicacion.queries.base import ClienteQueryBaseHandler
from clientes.modulos.clientes.dominio.entidades import Cliente
from clientes.modulos.clientes.dominio.repositorios import RepositorioClientes
from clientes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from clientes.seedwork.aplicacion.queries import ejecutar_query as query
from clientes.seedwork.dominio.entidades import Entidad

@dataclass
class ObtenerTodosCliente(Query):
    id: str

    
class ObtenerTodasClientesHandler(ClienteQueryBaseHandler):

    def handle(self) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)
        cliente =  self.fabrica_clientes.crear_objeto(repositorio.obtener_todos(), MapeadorCliente())
        return QueryResultado(resultado=cliente)


class ObtenerClienteHandler(ClienteQueryBaseHandler):

    def handle(self, query) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)

        entidades: list[Entidad] = repositorio.obtener_todos()
        clientes: list[ClienteDTO]
        for entidad in entidades:
            cliente =  self.fabrica_clientes.crear_objeto(entidad, MapeadorCliente())
        return QueryResultado(resultado=cliente)

@query.register(ObtenerTodosCliente)
def ejecutar_query_obtener_todos_cliente(query: ObtenerTodosCliente):
    handler = ObtenerClienteHandler()
    return handler.handle(query)