from ._constants import BIN_OP_SPECIAL_CASES
from typing import Any


def get_bin_conversion(op_name: str) -> str:
    return BIN_OP_SPECIAL_CASES.get(op_name, op_name.lower())


def get_cls_name_of(obj: Any) -> str:
    cls = type(obj)
    return cls.__name__
