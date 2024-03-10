import datetime
from inquilinos.modulos.inquilinos.dominio.objetos_valor import Genero
from inquilinos.seedwork.aplicacion.comandos import Comando
from inquilinos.modulos.inquilinos.aplicacion.dto import InquilinoDTO
from inquilinos.seedwork.dominio.objetos_valor import Direccion, TipoContacto
from .base import CrearInquilinoBaseHandler
from dataclasses import dataclass, field
from inquilinos.seedwork.aplicacion.comandos import ejecutar_commando as comando

from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino
from inquilinos.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from inquilinos.modulos.inquilinos.aplicacion.mapeadores import MapeadorInquilino
from inquilinos.modulos.inquilinos.infraestructura.repositorios import RepositorioInquilinos

@dataclass
class CrearInquilino(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombres: str
    apellidos: str
    identificacion: str
    fecha_nacimiento: str
    genero: str
    id_cor: str
    direccion: str
    telefono: str
    correo: str
    sitioWeb: str

class CrearInquilinoHandler(CrearInquilinoBaseHandler):
    
    def handle(self, comando: CrearInquilino):
        inquilino_dto = InquilinoDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,    nombres=comando.nombres
            ,    apellidos=comando.apellidos
            ,    identificacion=comando.identificacion
            ,    fecha_nacimiento=comando.fecha_nacimiento
            ,    genero=comando.genero
            ,    id_cor=comando.id_cor
            ,    direccion=comando.direccion
            ,    telefono=comando.telefono
            ,    correo=comando.correo
            ,    sitioWeb=comando.sitioWeb)

        inquilino: Inquilino = self.fabrica_inquilinos.crear_objeto(inquilino_dto, MapeadorInquilino())
        inquilino.crear_inquilino(inquilino)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInquilinos.__class__)
        UnidadTrabajoPuerto.limpiar()
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, inquilino)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearInquilino)
def ejecutar_comando_crear_inquilino(comando: CrearInquilino):
    handler = CrearInquilinoHandler()
    handler.handle(comando)
    