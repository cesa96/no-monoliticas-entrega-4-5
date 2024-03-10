""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from propiedades.seedwork.dominio.repositorios import Mapeador
from propiedades.modulos.propiedades.dominio.objetos_valor import bool, TipoPropiedad
from propiedades.modulos.propiedades.dominio.entidades import  Propiedad
from .dto import Propiedad as PropiedadDTO
from propiedades.seedwork.dominio.objetos_valor import float, Direccion, TipoContacto

class MapeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        
        propiedad_dto = PropiedadDTO()
        propiedad_dto.fecha_creacion = entidad.fecha_creacion
        propiedad_dto.fecha_actualizacion = entidad.fecha_actualizacion
        propiedad_dto.id = str(entidad.id)
        propiedad_dto.nombre = entidad.nombre
        propiedad_dto.descripcion = entidad.descripcion
        propiedad_dto.id_cor = entidad.id_cor
        propiedad_dto.num_habitaciones = entidad.num_habitaciones
        propiedad_dto.num_banos = entidad.num_banos
        propiedad_dto.fecha_construccion = entidad.fecha_construccion
        propiedad_dto.fecha_modernizacion = entidad.fecha_modernizacion
        propiedad_dto.disponible = entidad.disponible
        propiedad_dto.direccion = entidad.direccion.direccion
        propiedad_dto.precio= entidad.precio
        propiedad_dto.metrosCuadrados= entidad.metrosCuadrados
        propiedad_dto.tipoPropiedad = entidad.tipoPropiedad
        propiedad_dto.servicios =entidad.servicios

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        direccion  = Direccion(None, None, dto.direccion)
        propiedad = Propiedad(id=dto.id,  nombre=dto.nombre,descripcion=dto.descripcion, 
                          num_habitaciones=dto.num_habitaciones,num_banos=dto.num_banos,  fecha_construccion=dto.fecha_construccion, 
                          fecha_modernizacion=dto.fecha_modernizacion, disponible=dto.disponible, direccion=direccion, precio=dto.precio, 
                          metrosCuadrados=dto.metrosCuadrados, tipoPropiedad=dto.tipoPropiedad, servicios=dto.servicios, id_cor=dto.id_cor)
        propiedad.direccion = direccion
        
        return propiedad
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__