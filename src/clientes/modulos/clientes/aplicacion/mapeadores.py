from clientes.seedwork.aplicacion.dto import Mapeador as AppMap
from clientes.seedwork.dominio.objetos_valor import DatoContacto, Direccion, TipoContacto
from clientes.seedwork.dominio.repositorios import Mapeador as RepMap
from clientes.modulos.clientes.dominio.entidades import Cliente

from .dto import ClienteDTO

from datetime import datetime



class MapeadorClienteDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> ClienteDTO:
        cliente_dto = ClienteDTO(nombres= externo.get('nombres'), 
                                 apellidos = externo.get('apellidos'),
                                 identificacion = externo.get('identificacion'),                                
                                 fecha_nacimiento = externo.get('fecha_nacimiento'),                                
                                 genero = externo.get('genero'),                                
                                 direccion = externo.get('direccion'),                                
                                 telefono = externo.get('telefono'),                                
                                 correo = externo.get('correo'),                                
                                 tipoCliente = externo.get('tipoCliente'),                                
                                 sitioWeb = externo.get('sitioWeb'),                                
                                 
                                 )
#        cliente_dto.fecha_creacion = externo.fecha_creacion
#        cliente_dto.fecha_actualizacion = externo.fecha_actualizacion
#        cliente_dto.id = str(externo.id)
        return cliente_dto




    def dto_a_externo(self, dto: ClienteDTO) -> dict:
        return dto.__dict__


class MapeadorCliente(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def obtener_tipo(self) -> type:
        return Cliente.__class__

        

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        
        cliente_dto = ClienteDTO(fecha_creacion = entidad.fecha_creacion,
                fecha_actualizacion = entidad.fecha_actualizacion,
                id = entidad.id,
                nombres = entidad.nombres,
                apellidos = entidad.apellidos,
                identificacion = entidad.identificacion,
                fecha_nacimiento = entidad.fecha_nacimiento,
                genero = entidad.genero,
                tipoCliente = entidad.tipoCliente,
                sitioWeb =entidad.sitioWeb,
                telefono=entidad.telefono.contacto,
                correo=entidad.correo.contacto,
                direccion=entidad.direccion.direccion
                )


        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente = Cliente()
        direccion  = Direccion(None, None, dto.direccion)
        telefono = DatoContacto(None, TipoContacto.PHONE, dto.telefono)
        correo = DatoContacto(None, TipoContacto.MAIL, dto.correo)
        cliente = Cliente(id=dto.id, nombres=dto.nombres,apellidos=dto.apellidos, 
                          identificacion=dto.identificacion, fecha_nacimiento=dto.fecha_nacimiento, genero=dto.genero, direccion=direccion, telefono=telefono, 
                          correo=correo, tipoCliente=dto.tipoCliente, sitioWeb=dto.sitioWeb)
        cliente.telefono = telefono
        cliente.correo = correo
        cliente.direccion = direccion

        return cliente



