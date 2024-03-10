from inquilinos.seedwork.aplicacion.dto import Mapeador as AppMap
from inquilinos.seedwork.dominio.objetos_valor import DatoContacto, Direccion, TipoContacto
from inquilinos.seedwork.dominio.repositorios import Mapeador as RepMap
from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino, PropiedadInquilino

from .dto import InquilinoDTO, PropiedadesInquilinoDTO

from datetime import datetime



class MapeadorInquilinoDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> InquilinoDTO:
        inquilino_dto = InquilinoDTO(nombres= externo.get('nombres'), 
                                 apellidos = externo.get('apellidos'),
                                 identificacion = externo.get('identificacion'),                                
                                 fecha_nacimiento = externo.get('fecha_nacimiento'),                                
                                 genero = externo.get('genero'),                                
                                 id_cor = externo.get('id_cor'),                                
                                 direccion = externo.get('direccion'),                                
                                 telefono = externo.get('telefono'),                                
                                 correo = externo.get('correo'),                                                            
                                 sitioWeb = externo.get('sitioWeb'),                                
                                 
                                 )
#        inquilino_dto.fecha_creacion = externo.fecha_creacion
#        inquilino_dto.fecha_actualizacion = externo.fecha_actualizacion
#        inquilino_dto.id = str(externo.id)
        return inquilino_dto




    def dto_a_externo(self, dto: InquilinoDTO) -> dict:
        return dto.__dict__


class MapeadorInquilino(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def obtener_tipo(self) -> type:
        return Inquilino.__class__

        

    def entidad_a_dto(self, entidad: Inquilino) -> InquilinoDTO:

        propiedades = list()
        for prop in entidad.propiedades:
            propiedadDto = PropiedadesInquilinoDTO(id=prop.id, id_inquilino=entidad.id, id_propiedad=prop.id_propiedad)
            propiedades.append(propiedadDto)
        
        inquilino_dto = InquilinoDTO(fecha_creacion = entidad.fecha_creacion,
                fecha_actualizacion = entidad.fecha_actualizacion,
                id = entidad.id,
                nombres = entidad.nombres,
                apellidos = entidad.apellidos,
                identificacion = entidad.identificacion,
                fecha_nacimiento = entidad.fecha_nacimiento,
                genero = entidad.genero,
                id_cor = entidad.id_cor,
                sitioWeb =entidad.sitioWeb,
                telefono=entidad.telefono.contacto,
                correo=entidad.correo.contacto,
                direccion=entidad.direccion.direccion,
                propiedades = propiedades
                )


        return inquilino_dto

    def dto_a_entidad(self, dto: InquilinoDTO) -> Inquilino:
        inquilino = Inquilino()
        direccion  = Direccion(None, None, dto.direccion)
        telefono = DatoContacto(None, TipoContacto.PHONE, dto.telefono)
        correo = DatoContacto(None, TipoContacto.MAIL, dto.correo)
        inquilino = Inquilino(id=dto.id, nombres=dto.nombres,apellidos=dto.apellidos, 
                          identificacion=dto.identificacion, fecha_nacimiento=dto.fecha_nacimiento, genero=dto.genero, direccion=direccion, telefono=telefono, 
                          correo=correo, sitioWeb=dto.sitioWeb, id_cor=dto.id_cor)
        inquilino.telefono = telefono
        inquilino.correo = correo
        inquilino.direccion = direccion
        inquilino.propiedades = list()
        for prop in dto.propiedades:
            inquilino.propiedades.append(PropiedadInquilino(id_propiedad=prop.id_propiedad))




        return inquilino



