"""Objetos valor del dominio de propiedades

En este archivo usted encontrará los objetos valor del dominio de propiedades

"""

from __future__ import annotations

from dataclasses import dataclass, field
from propiedades.seedwork.dominio.objetos_valor import ObjetoValor, Codigo
from datetime import datetime
from enum import Enum


class TipoPropiedad(Enum):
    CASA = "Casa"
    APARTAMENTO = "Apartamento"
    ASESORIA = "Asesoria Inquilinos"
    PERITO = "Perito"
    FIINANCIERAS = "Instituciones financieras"
    GOBIERNO = "Instituciones gubernamentales"

class bool(Enum):
    MALE = "Masculino"
    FEMALE = "Femenino"
    NO_INFORM = "No informa"

