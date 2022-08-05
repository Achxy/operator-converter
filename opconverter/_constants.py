from __future__ import annotations
from typing import Final


BIN_OP_SPECIAL_CASES: Final[dict[str, str]] = {
    "Mult": "mul",
    "Div": "truediv",
    "BitOr": "or_",
    "BitXor": "xor",
    "BitAnd": "and_",
    "MatMult": "matmul",
}
CMP_SPECIAL_CASES: Final[dict[str, str]] = {
    "NotEq": "ne",
    "LtE": "le",
    "GtE": "ge",
    "Is": "is_",
    "IsNot": "is_not",
    "In": "contains",
    # NotIn does not have a direct implementation in stdlib `operator`
}
DUNDER_FUTURE_IMPORT: Final[str] = "__future__"
