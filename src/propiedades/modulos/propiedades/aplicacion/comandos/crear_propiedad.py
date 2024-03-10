import datetime
from propiedades.modulos.propiedades.dominio.objetos_valor import bool, TipoPropiedad
from propiedades.seedwork.aplicacion.comandos import Comando
from propiedades.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedades.seedwork.dominio.objetos_valor import Direccion, TipoContacto
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando as comando

from propiedades.modulos.propiedades.dominio.entidades import Propiedad
from propiedades.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedades.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedades.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades

@dataclass
class CrearPropiedad(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombre: str
    descripcion: str
    id_cor: str
    num_habitaciones: int
    num_banos: int
    fecha_construccion: str
    fecha_modernizacion: str
    disponible: bool
    direccion: str
    precio: float
    metrosCuadrados: float
    tipoPropiedad: str
    servicios: str

class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,    nombre=comando.nombre
            ,    descripcion=comando.descripcion
            ,    id_cor=comando.id_cor
            ,    num_habitaciones=comando.num_habitaciones
            ,    num_banos=comando.num_banos
            ,    fecha_construccion=comando.fecha_construccion
            ,    fecha_modernizacion=comando.fecha_modernizacion
            ,    disponible=comando.disponible
            ,    direccion=comando.direccion
            ,    precio=comando.precio
            ,    metrosCuadrados=comando.metrosCuadrados
            ,    tipoPropiedad=comando.tipoPropiedad
            ,    servicios=comando.servicios)

        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        UnidadTrabajoPuerto.limpiar()
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
    