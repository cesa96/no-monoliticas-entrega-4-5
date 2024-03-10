from propiedades.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedades.seedwork.dominio.objetos_valor import float, Direccion, TipoContacto
from propiedades.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedades.modulos.propiedades.dominio.entidades import Propiedad

from .dto import PropiedadDTO

from datetime import datetime



class MapeadorPropiedadDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO(nombre= externo.get('nombre'), 
                                 descripcion = externo.get('descripcion'),
                                 id_cor = externo.get('id_cor'),
                                 num_habitaciones = externo.get('num_habitaciones'),                                
                                 num_banos = externo.get('num_banos'),                                
                                 fecha_construccion = externo.get('fecha_construccion'),                                
                                 fecha_modernizacion = externo.get('fecha_modernizacion'),                                
                                 disponible = externo.get('disponible'),                                
                                 direccion = externo.get('direccion'),                                
                                 precio = externo.get('precio'),                                
                                 metrosCuadrados = externo.get('metrosCuadrados'),                                
                                 tipoPropiedad = externo.get('tipoPropiedad'),                                
                                 servicios = externo.get('servicios'),                                
                                 
                                 )
#        propiedad_dto.fecha_creacion = externo.fecha_creacion
#        propiedad_dto.fecha_actualizacion = externo.fecha_actualizacion
#        propiedad_dto.id = str(externo.id)
        return propiedad_dto




    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def obtener_tipo(self) -> type:
        return Propiedad.__class__

        

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        
        propiedad_dto = PropiedadDTO(fecha_creacion = entidad.fecha_creacion,
                fecha_actualizacion = entidad.fecha_actualizacion,
                id = entidad.id,
                nombre = entidad.nombre,
                descripcion = entidad.descripcion,
                id_cor = entidad.id_cor,
                num_habitaciones = entidad.num_habitaciones,
                num_banos = entidad.num_banos,
                fecha_construccion = entidad.fecha_construccion,
                fecha_modernizacion = entidad.fecha_modernizacion,
                disponible = entidad.disponible,
                tipoPropiedad = entidad.tipoPropiedad,
                servicios =entidad.servicios,
                precio=entidad.precio,
                metrosCuadrados=entidad.metrosCuadrados,
                direccion=entidad.direccion.direccion
                )


        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        direccion  = Direccion(None, None, dto.direccion)
        propiedad = Propiedad(id=dto.id, nombre=dto.nombre,descripcion=dto.descripcion, 
                          num_habitaciones=dto.num_habitaciones, num_banos=dto.num_banos, fecha_construccion=dto.fecha_construccion, fecha_modernizacion=dto.fecha_modernizacion
                          , disponible=dto.disponible, direccion=direccion, precio=dto.precio, 
                          metrosCuadrados=dto.metrosCuadrados, tipoPropiedad=dto.tipoPropiedad, servicios=dto.servicios, id_cor=dto.id_cor)
        propiedad.direccion = direccion

        return propiedad



