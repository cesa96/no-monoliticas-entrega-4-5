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
class EliminarInquilino(Comando):
    id_inquilino: str
    id_cor: str


class EliminarInquilinoHandler(CrearInquilinoBaseHandler):
    
    def handle(self, comando: EliminarInquilino):

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInquilinos.__class__)
        inquilino: Inquilino =  repositorio.obtener_por_id(comando.id_inquilino)
        inquilino.eliminar_inquilino()
        print(f'Id inquilino 1: {str(inquilino.id)}')
        UnidadTrabajoPuerto.limpiar()
        UnidadTrabajoPuerto.registrar_batch(repositorio.eliminar, inquilino)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(EliminarInquilino)
def ejecutar_comando_eliminar_inquilino(comando: EliminarInquilino):
    handler = EliminarInquilinoHandler()
    handler.handle(comando)
    