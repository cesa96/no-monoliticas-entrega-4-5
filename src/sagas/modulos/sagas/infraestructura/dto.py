"""DTOs para la capa de infrastructura del dominio de sagas

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de sagas

"""

from sagas.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Saga(db.Model):
    __tablename__ = "sagas"
    id = db.Column(db.String(100), primary_key=True)
    fecha_creacion = db.Column(db.String(30), nullable=False)
    fecha_actualizacion = db.Column(db.String(30), nullable=False)
    id_inquilino =     db.Column(db.String(100), nullable=True)
    id_propiedad =     db.Column(db.String(100), nullable=True)
    dataInquilino =     db.Column(db.Text, nullable=True)
    dataPropiedad =     db.Column(db.Text, nullable=True)
