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
from ast import (
    And,
    Assign,
    AugAssign,
    BinOp,
    BoolOp,
    Call,
    Compare,
    Load,
    Name,
    UnaryOp,
)

from ._constants import AUGMENT, FIRST
from ._helpers import (
    get_bin_conversion,
    get_cls_name_of,
    get_cmp_conversion,
    get_unary_conversion,
    recursively_convert_inner_nodes,
)
from .abstract import AbstractBaseStandardOperationFunctionNodeTransformer


class OperationNodeTransformer(AbstractBaseStandardOperationFunctionNodeTransformer):
    __slots__ = ()

    def visit_AugAssign(self, node: AugAssign) -> Assign:
        op = AUGMENT + get_bin_conversion(get_cls_name_of(node.op))
        left, right = node.target, node.value
        self._extend_import_symbols(op)
        converted = recursively_convert_inner_nodes(
            Assign(
                targets=[node.target],
                value=Call(
                    func=Name(id=op, ctx=Load()),
                    args=[left, right],
                    keywords=[],
                ),
            )
        )
        self._extend_import_symbols(*converted.operator_import_symbols)
        return converted.result

    def visit_BinOp(self, node: BinOp) -> Call:
        op = get_bin_conversion(get_cls_name_of(node.op))
        left, right = node.left, node.right
        self._extend_import_symbols(op)
        converted = recursively_convert_inner_nodes(
            Call(
                func=Name(id=op, ctx=Load()),
                args=[left, right],
                keywords=[],
            )
        )
        self._extend_import_symbols(*converted.operator_import_symbols)
        return converted.result

    def visit_Compare(self, node: Compare) -> Call:
        flat, comparators = [node.left] + node.comparators, []
        for current, next, cmp_ops in zip(flat, flat[FIRST:], node.ops):
            op = get_cmp_conversion(get_cls_name_of(cmp_ops))
            self._extend_import_symbols(op)
            comparators.append(
                Call(
                    func=Name(id=op, ctx=Load()),
                    args=[current, next],
                    keywords=[],
                )
            )
        converted = recursively_convert_inner_nodes(
            BoolOp(op=And(), values=comparators)
        )
        self._extend_import_symbols(*converted.operator_import_symbols)
        return converted.result

    def visit_UnaryOp(self, node: UnaryOp):
        op = get_unary_conversion(get_cls_name_of(node.op))
        self._extend_import_symbols(op)
        converted = recursively_convert_inner_nodes(
            Call(func=Name(id=op, ctx=Load()), args=[node.operand], keywords=[])
        )
        self._extend_import_symbols(*converted.operator_import_symbols)
        return converted.result
