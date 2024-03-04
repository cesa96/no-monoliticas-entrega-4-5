"""Objetos valor del dominio de inquilinos

En este archivo usted encontrará los objetos valor del dominio de inquilinos

"""

from __future__ import annotations

from dataclasses import dataclass, field
from inquilinos.seedwork.dominio.objetos_valor import ObjetoValor, Codigo
from datetime import datetime
from enum import Enum


class Genero(Enum):
    MALE = "Masculino"
    FEMALE = "Femenino"
    NO_INFORM = "No informa"

