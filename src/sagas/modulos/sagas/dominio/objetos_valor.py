"""Objetos valor del dominio de sagas

En este archivo usted encontrará los objetos valor del dominio de sagas

"""

from __future__ import annotations

from dataclasses import dataclass, field
from sagas.seedwork.dominio.objetos_valor import ObjetoValor, Codigo
from datetime import datetime
from enum import Enum


class TipoSaga(Enum):
    INVERSION = "Grupo de Inversión"
    AGENCIA = "Agencia Representación"
    ASESORIA = "Asesoria Inquilinos"
    PERITO = "Perito"
    FIINANCIERAS = "Instituciones financieras"
    GOBIERNO = "Instituciones gubernamentales"

class Genero(Enum):
    MALE = "Masculino"
    FEMALE = "Femenino"
    NO_INFORM = "No informa"

