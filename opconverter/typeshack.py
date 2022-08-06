from typing import TypeVar
from ast import AST


AST_co = TypeVar("AST_co", bound=AST, covariant=True)
