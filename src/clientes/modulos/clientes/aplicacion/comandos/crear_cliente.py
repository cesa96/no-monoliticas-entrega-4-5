import datetime
from clientes.modulos.clientes.dominio.objetos_valor import Genero, TipoCliente
from clientes.seedwork.aplicacion.comandos import Comando
from clientes.modulos.clientes.aplicacion.dto import ClienteDTO
from clientes.seedwork.dominio.objetos_valor import Direccion, TipoContacto
from .base import CrearClienteBaseHandler
from dataclasses import dataclass, field
from clientes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from clientes.modulos.clientes.dominio.entidades import Cliente
from clientes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from clientes.modulos.clientes.aplicacion.mapeadores import MapeadorCliente
from clientes.modulos.clientes.infraestructura.repositorios import RepositorioClientes

@dataclass
class CrearCliente(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombres: str
    apellidos: str
    identificacion: str
    fecha_nacimiento: str
    genero: str
    direccion: str
    telefono: str
    correo: str
    tipoCliente: str
    sitioWeb: str

class CrearClienteHandler(CrearClienteBaseHandler):
    
    def handle(self, comando: CrearCliente):
        cliente_dto = ClienteDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,    nombres=comando.nombres
            ,    apellidos=comando.apellidos
            ,    identificacion=comando.identificacion
            ,    fecha_nacimiento=comando.fecha_nacimiento
            ,    genero=comando.genero
            ,    direccion=comando.direccion
            ,    telefono=comando.telefono
            ,    correo=comando.correo
            ,    tipoCliente=comando.tipoCliente
            ,    sitioWeb=comando.sitioWeb)

        cliente: Cliente = self.fabrica_clientes.crear_objeto(cliente_dto, MapeadorCliente())
        cliente.crear_cliente(cliente)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)
        UnidadTrabajoPuerto.limpiar()
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, cliente)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearCliente)
def ejecutar_comando_crear_cliente(comando: CrearCliente):
    handler = CrearClienteHandler()
    handler.handle(comando)
    