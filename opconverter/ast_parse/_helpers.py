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
from ast import Name, Load, Call, keyword
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


def form_keywords_from_dict(mapping: dict) -> list[keyword]:
    return [keyword(arg=arg, value=value) for arg, value, in mapping.items()]


def Function(name, *_args, args=[], keywords=[], **_kwargs):
    err = "{} arguments and `{}` kwarg cannot be simultaneously be provided"
    if _args and args:
        raise ValueError(err.format("Positional", "args"))
    if keywords and _kwargs:
        raise ValueError(err.format("Keyword", "keywords"))
    return Call(
        func=Name(id=name, ctx=Load()),
        args=args or _args,
        keywords=keywords or form_keywords_from_dict(_kwargs),
    )
