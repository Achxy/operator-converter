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
DUNDER_FUTURE_IMPORT: Final[str] = "__future__"
