"""DTOs para la capa de infrastructura del dominio de inquilinos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de inquilinos

"""

from inquilinos.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class PropiedadesInquilino(db.Model):
    __tablename__ = "propiedades_inquilinos"
    id = db.Column(db.String(100), primary_key=True)
    id_propiedad = db.Column(db.String(100), nullable=False)
    id_inquilino = db.Column(db.String(100), ForeignKey("inquilinos.id"))


class Inquilino(db.Model):
    __tablename__ = "inquilinos"
    id = db.Column(db.String(100), primary_key=True)
    fecha_creacion = db.Column(db.String(30), nullable=False)
    fecha_actualizacion = db.Column(db.String(30), nullable=False)
    nombres = db.Column(db.String(100), nullable=True)
    apellidos = db.Column(db.String(100), nullable=True)
    identificacion = db.Column(db.String(20), nullable=True)
    fecha_nacimiento = db.Column(db.String(20), nullable=True)
    genero = db.Column(db.String(50), nullable=True)
    id_cor = db.Column(db.String(100), nullable=True)
    direccion = db.Column(db.String(150), nullable=True)
    telefono  = db.Column(db.String(20), nullable=True)
    correo  = db.Column(db.String(150), nullable=True)
    sitioWeb = db.Column(db.String(200), nullable=True)
    propiedades = db.relationship('PropiedadesInquilino', backref='inquilinos')

