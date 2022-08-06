from .abstract import AbstractStandardOperationFunctionTransformer
from ast import AugAssign, Name, Assign, BinOp, Compare, Call, Load, BoolOp, And
from ._import_helper import add_ImportFromNode
from ._helpers import (
    get_bin_conversion,
    get_cls_name_of,
    get_cmp_conversion,
    recursively_convert_inner_nodes,
)
from ._constants import AUGMENT


class OperationNodeTransformer(AbstractStandardOperationFunctionTransformer):
    def visit_AugAssign(self, node: AugAssign) -> Assign:
        op_name = AUGMENT + get_bin_conversion(get_cls_name_of(node.op))
        left, right = node.target, node.value
        self._extend_import_symbols(op_name)
        converted = recursively_convert_inner_nodes(
            Assign(
                targets=[node.target],
                value=Call(
                    func=Name(id=op_name, ctx=Load()),
                    args=[left, right],
                    keywords=[],
                ),
            )
        )
        self._extend_import_symbols(*converted.operator_import_symbols)
        return converted.result

    def visit_BinOp(self, node: BinOp) -> Call:
        left, right = node.left, node.right
        op_name = get_bin_conversion(get_cls_name_of(node.op))
        self._extend_import_symbols(op_name)
        converted = recursively_convert_inner_nodes(
            Call(
                func=Name(id=op_name, ctx=Load()),
                args=[left, right],
                keywords=[],
            )
        )
        self._extend_import_symbols(*converted.operator_import_symbols)
        return converted.result

    def visit_Compare(self, node: Compare) -> Call:
        flat = [node.left] + node.comparators
        new_comparators = []
        for current, next, cmp_ops in zip(flat, flat[1:], node.ops):
            cmp_name = get_cmp_conversion(get_cls_name_of(cmp_ops))
            self._extend_import_symbols(cmp_name)
            new_comparators.append(
                Call(
                    func=Name(id=cmp_name, ctx=Load()),
                    args=[current, next],
                    keywords=[],
                )
            )
        converted = recursively_convert_inner_nodes(
            BoolOp(op=And(), values=new_comparators)
        )
        self._extend_import_symbols(*converted.operator_import_symbols)
        return converted.result
