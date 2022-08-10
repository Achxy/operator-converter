"""
ConvertOperator is a project for converting standard operations to functions
Copyright (C) 2022-present  Achxy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from typing import Final, Literal

from ..typeshack import SpecialCase

BIN_OP_SPECIAL_CASES: SpecialCase = {
    "Mult": "mul",
    "Div": "truediv",
    "BitOr": "or_",
    "BitXor": "xor",
    "BitAnd": "and_",
    "MatMult": "matmul",
}
CMP_SPECIAL_CASES: SpecialCase = {
    "NotEq": "ne",
    "LtE": "le",
    "GtE": "ge",
    "Is": "is_",
    "IsNot": "is_not",
    "In": "contains",
    # NotIn does not have a direct implementation in stdlib `operator`
}
UNARY_OP_SPECIAL_CASES: SpecialCase = {
    "UAdd": "pos",
    "USub": "neg",
    "Not": "not_",
}

DUNDER_FUTURE_IMPORT: Final[str] = "__future__"
AUGMENT: Final[str] = "i"

FIRST: Final[Literal[1]] = 1
OPERATOR_GETITEM: Final[str] = "getitem"
OPERATOR_DELITEM: Final[str] = "delitem"
