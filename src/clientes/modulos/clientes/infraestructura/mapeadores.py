""" Mapeadores para la capa de infrastructura del dominio de clientes

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from clientes.seedwork.dominio.repositorios import Mapeador
from clientes.modulos.clientes.dominio.objetos_valor import Genero, TipoCliente
from clientes.modulos.clientes.dominio.entidades import  Cliente
from .dto import Cliente as ClienteDTO
from clientes.seedwork.dominio.objetos_valor import DatoContacto, Direccion, TipoContacto

class MapeadorCliente(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        
        cliente_dto = ClienteDTO()
        cliente_dto.fecha_creacion = entidad.fecha_creacion
        cliente_dto.fecha_actualizacion = entidad.fecha_actualizacion
        cliente_dto.id = str(entidad.id)
        cliente_dto.nombres = entidad.nombres
        cliente_dto.apellidos = entidad.apellidos
        cliente_dto.identificacion = entidad.identificacion
        cliente_dto.fecha_nacimiento = entidad.fecha_nacimiento
        cliente_dto.genero = entidad.genero
        cliente_dto.direccion = entidad.direccion.direccion
        cliente_dto.telefono= entidad.telefono.contacto
        cliente_dto.correo= entidad.correo.contacto
        cliente_dto.tipoCliente = entidad.tipoCliente
        cliente_dto.sitioWeb =entidad.sitioWeb

        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        direccion  = Direccion(None, None, dto.direccion)
        telefono = DatoContacto(None, TipoContacto.PHONE, dto.telefono)
        correo = DatoContacto(None, TipoContacto.MAIL, dto.correo)
        cliente = Cliente(id=dto.id,  nombres=dto.nombres,apellidos=dto.apellidos, 
                          identificacion=dto.identificacion, fecha_nacimiento=dto.fecha_nacimiento, genero=dto.genero, direccion=direccion, telefono=telefono, 
                          correo=correo, tipoCliente=dto.tipoCliente, sitioWeb=dto.sitioWeb)
        cliente.telefono = telefono
        cliente.correo = correo
        cliente.direccion = direccion
        
        return cliente
    
    def obtener_tipo(self) -> type:
        return Cliente.__class__