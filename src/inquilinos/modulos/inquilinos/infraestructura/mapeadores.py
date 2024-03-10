""" Mapeadores para la capa de infrastructura del dominio de inquilinos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from inquilinos.seedwork.dominio.repositorios import Mapeador
from inquilinos.modulos.inquilinos.dominio.objetos_valor import Genero
from inquilinos.modulos.inquilinos.dominio.entidades import  Inquilino, PropiedadInquilino
from .dto import Inquilino as InquilinoDTO, PropiedadesInquilino as PropiedadesInquilinoDto
from inquilinos.seedwork.dominio.objetos_valor import DatoContacto, Direccion, TipoContacto

class MapeadorInquilino(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def entidad_a_dto(self, entidad: Inquilino) -> InquilinoDTO:
        
        inquilino_dto = InquilinoDTO()
        inquilino_dto.fecha_creacion = entidad.fecha_creacion
        inquilino_dto.fecha_actualizacion = entidad.fecha_actualizacion
        inquilino_dto.id = str(entidad.id)
        inquilino_dto.nombres = entidad.nombres
        inquilino_dto.apellidos = entidad.apellidos
        inquilino_dto.identificacion = entidad.identificacion
        inquilino_dto.fecha_nacimiento = entidad.fecha_nacimiento
        inquilino_dto.genero = entidad.genero
        inquilino_dto.id_cor = entidad.id_cor
        inquilino_dto.direccion = entidad.direccion.direccion
        inquilino_dto.telefono= entidad.telefono.contacto
        inquilino_dto.correo= entidad.correo.contacto
        inquilino_dto.sitioWeb =entidad.sitioWeb

        propiedades_dto = list()
        for propiedad in entidad.propiedades:
            propiedadDto = PropiedadesInquilinoDto()
            propiedadDto.id = propiedad.id
            propiedadDto.id_inquilino = entidad.id
            propiedadDto.id_propiedad = propiedad.id_propiedad
            propiedades_dto.append(propiedadDto)

        
        inquilino_dto.propiedades = propiedades_dto

        return inquilino_dto

    def dto_a_entidad(self, dto: InquilinoDTO) -> Inquilino:
        direccion  = Direccion(None, None, dto.direccion)
        telefono = DatoContacto(None, TipoContacto.PHONE, dto.telefono)
        correo = DatoContacto(None, TipoContacto.MAIL, dto.correo)
        print(f'Id inquilino dto: {str(dto.id)}')

        inquilino = Inquilino(id=dto.id,  nombres=dto.nombres,apellidos=dto.apellidos, 
                          identificacion=dto.identificacion, fecha_nacimiento=dto.fecha_nacimiento, genero=dto.genero, direccion=direccion, telefono=telefono, 
                          correo=correo, sitioWeb=dto.sitioWeb, id_cor=dto.id_cor)
        inquilino.telefono = telefono
        inquilino.correo = correo
        inquilino.direccion = direccion
        inquilino.id = dto.id

        inquilino.propiedades = list()

        propiedades_dto: list[PropiedadesInquilinoDto] = dto.propiedades
        propiedades = list()
        for propiedadDto in propiedades_dto:
            propiedad = PropiedadInquilino(id=propiedadDto.id, id_propiedad=propiedadDto.id_propiedad)
            propiedades.append(propiedad)
        inquilino.propiedades = propiedades
        return inquilino
    
    def obtener_tipo(self) -> type:
        return Inquilino.__class__