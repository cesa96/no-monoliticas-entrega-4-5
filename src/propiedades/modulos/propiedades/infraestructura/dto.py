"""DTOs para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de propiedades

"""

from propiedades.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id = db.Column(db.String(100), primary_key=True)
    fecha_creacion = db.Column(db.String(30), nullable=False)
    fecha_actualizacion = db.Column(db.String(30), nullable=False)
    nombre = db.Column(db.String(100), nullable=True)
    descripcion = db.Column(db.String(100), nullable=True)
    num_habitaciones = db.Column(db.Integer, nullable=True)
    id_cor = db.Column(db.String(100), nullable=True)
    num_banos = db.Column(db.Integer, nullable=True)
    fecha_construccion = db.Column(db.String(20), nullable=True)
    fecha_modernizacion = db.Column(db.String(20), nullable=True)
    disponible = db.Column(db.Boolean, nullable=True)
    direccion = db.Column(db.String(150), nullable=True)
    precio  = db.Column(db.Float, nullable=True)
    metrosCuadrados  = db.Column(db.Float, nullable=True)
    tipoPropiedad = db.Column(db.String(20), nullable=True)
    servicios = db.Column(db.String(200), nullable=True)

