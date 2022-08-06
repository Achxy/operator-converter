from .abstract import AbstractBaseStandardOperationFunctionNodeTransformer
from ast import AugAssign, Name, Assign, BinOp, Compare, Call, Load, BoolOp, And
from ._import_helper import add_ImportFromNode
from ._helpers import (
    get_bin_conversion,
    get_cls_name_of,
    get_cmp_conversion,
    recursively_convert_inner_nodes,
)
from ._constants import AUGMENT, FIRST


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
