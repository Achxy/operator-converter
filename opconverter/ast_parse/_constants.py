from typing import Final

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
FIRST: Final[int] = 1
