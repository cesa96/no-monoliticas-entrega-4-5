import datetime
from propiedades.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedadHandler
from propiedades.modulos.propiedades.dominio.objetos_valor import Genero
from propiedades.seedwork.aplicacion.comandos import Comando
from propiedades.modulos.propiedades.aplicacion.dto import propiedadDTO
from propiedades.seedwork.dominio.objetos_valor import Direccion, TipoContacto
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando as comando

from propiedades.modulos.propiedades.dominio.entidades import Propiedad
from propiedades.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedades.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedades.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades

@dataclass
class Eliminarpropiedad(Comando):
    id_propiedad: str
    id_cor: str


class EliminarpropiedadHandler(CrearPropiedadHandler):
    
    def handle(self, comando: Eliminarpropiedad):

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        propiedad: Propiedad =  repositorio.obtener_por_id(comando.id_propiedad)
        propiedad.eliminar_propiedad()
        print(f'Id propiedad 1: {str(propiedad.id)}')
        UnidadTrabajoPuerto.limpiar()
        UnidadTrabajoPuerto.registrar_batch(repositorio.eliminar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(Eliminarpropiedad)
def ejecutar_comando_eliminar_propiedad(comando: Eliminarpropiedad):
    handler = EliminarpropiedadHandler()
    handler.handle(comando)
    