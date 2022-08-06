from typing import Any

from ._constants import BIN_OP_SPECIAL_CASES, CMP_SPECIAL_CASES, UNARY_OP_SPECIAL_CASES


def get_bin_conversion(op_name: str) -> str:
    return BIN_OP_SPECIAL_CASES.get(op_name, op_name.lower())


def get_cmp_conversion(cmp_name: str) -> str:
    if cmp_name == "NotIn":
        msg = "NotIn does not have a direct implementation in stdlib `operator`"
        raise ValueError(msg)
    return CMP_SPECIAL_CASES.get(cmp_name, cmp_name.lower())


def get_unary_conversion(op_name: str) -> str:
    return UNARY_OP_SPECIAL_CASES.get(op_name, op_name.lower())


def get_cls_name_of(obj: Any) -> str:
    cls = type(obj)
    return cls.__name__


def recursively_convert_inner_nodes(node):
    from .parser import StandardOperationFunctionNodeTransformer

    new = StandardOperationFunctionNodeTransformer(node)
    return new
