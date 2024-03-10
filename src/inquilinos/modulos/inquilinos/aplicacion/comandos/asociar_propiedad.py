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
class AsociarPropiedad(Comando):
    id_inquilino: str
    id_propiedad: str
    id_cor: str


class AsociarPropiedadHandler(CrearInquilinoBaseHandler):
    
    def handle(self, comando: AsociarPropiedad):

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInquilinos.__class__)
        inquilino: Inquilino =  repositorio.obtener_por_id(comando.id_inquilino)
        print(f'Id inquilino 1: {str(inquilino.id)}')
        inquilino.asociar_propiedad(comando.id_propiedad)
        UnidadTrabajoPuerto.limpiar()
        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, inquilino)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(AsociarPropiedad)
def ejecutar_comando_crear_inquilino(comando: AsociarPropiedad):
    handler = AsociarPropiedadHandler()
    handler.handle(comando)
    