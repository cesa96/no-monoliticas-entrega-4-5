# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: propiedades.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11propiedades.proto\x12\x0bpropiedades\x1a\x1fgoogle/protobuf/timestamp.proto\"\x99\x05\n\tPropiedad\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0e\x66\x65\x63ha_creacion\x18\x02 \x01(\tH\x01\x88\x01\x01\x12 \n\x13\x66\x65\x63ha_actualizacion\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x13\n\x06nombre\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x18\n\x0b\x64\x65scripcion\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1d\n\x10num_habitaciones\x18\x06 \x01(\x05H\x05\x88\x01\x01\x12\x16\n\tnum_banos\x18\x07 \x01(\x05H\x06\x88\x01\x01\x12\x1f\n\x12\x66\x65\x63ha_construccion\x18\x08 \x01(\tH\x07\x88\x01\x01\x12 \n\x13\x66\x65\x63ha_modernizacion\x18\t \x01(\tH\x08\x88\x01\x01\x12\x17\n\ndisponible\x18\n \x01(\x08H\t\x88\x01\x01\x12\x16\n\tdireccion\x18\x0b \x01(\tH\n\x88\x01\x01\x12\x13\n\x06precio\x18\x0c \x01(\x02H\x0b\x88\x01\x01\x12\x1d\n\x10metros_cuadrados\x18\r \x01(\x02H\x0c\x88\x01\x01\x12\x1a\n\rtipoPropiedad\x18\x0e \x01(\tH\r\x88\x01\x01\x12\x16\n\tservicios\x18\x0f \x01(\tH\x0e\x88\x01\x01\x42\x05\n\x03_idB\x11\n\x0f_fecha_creacionB\x16\n\x14_fecha_actualizacionB\t\n\x07_nombreB\x0e\n\x0c_descripcionB\x13\n\x11_num_habitacionesB\x0c\n\n_num_banosB\x15\n\x13_fecha_construccionB\x16\n\x14_fecha_modernizacionB\r\n\x0b_disponibleB\x0c\n\n_direccionB\t\n\x07_precioB\x13\n\x11_metros_cuadradosB\x10\n\x0e_tipoPropiedadB\x0c\n\n_servicios\"\x1c\n\x0eQueryPropiedad\x12\n\n\x02id\x18\x01 \x01(\t\"c\n\x12RespuestaPropiedad\x12\x0f\n\x07mensaje\x18\x01 \x01(\t\x12.\n\tpropiedad\x18\x02 \x01(\x0b\x32\x16.propiedades.PropiedadH\x00\x88\x01\x01\x42\x0c\n\n_propiedad2\xb0\x01\n\x0bPropiedades\x12K\n\x0e\x43rearPropiedad\x12\x16.propiedades.Propiedad\x1a\x1f.propiedades.RespuestaPropiedad\"\x00\x12T\n\x12\x43onsultarPropiedad\x12\x1b.propiedades.QueryPropiedad\x1a\x1f.propiedades.RespuestaPropiedad\"\x00\x42\x34\n\x18\x63o.edu.uniandes.misw4406B\x10PropiedadesProtoP\x01\xa2\x02\x03\x43LIb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'propiedades_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030co.edu.uniandes.misw4406B\020PropiedadesProtoP\001\242\002\003CLI'
  _PROPIEDAD._serialized_start=68
  _PROPIEDAD._serialized_end=733
  _QUERYPROPIEDAD._serialized_start=735
  _QUERYPROPIEDAD._serialized_end=763
  _RESPUESTAPROPIEDAD._serialized_start=765
  _RESPUESTAPROPIEDAD._serialized_end=864
  _PROPIEDADES._serialized_start=867
  _PROPIEDADES._serialized_end=1043
# @@protoc_insertion_point(module_scope)
