from .abstract import AbstractStandardOperationFunctionTransformer
from ast import AugAssign, Name, Assign, BinOp, Compare, Call, Load, BoolOp, And
from ._import_helper import add_ImportFromNode
from ._helpers import get_bin_conversion, get_cls_name_of, get_cmp_conversion
from ._constants import AUGMENT

# TODO: :)
TODO = """
class OperationNodeTransformer(AbstractStandardOperationFunctionTransformer):
    def visit_AugAssign(self, node: AugAssign) -> Assign:
        op_name = AUGMENT + get_bin_conversion(get_cls_name_of(node.op))
        left, right = node.target, node.value
        self._symbol_update(op_name)
        new_node = OperationNodeTransformer(
            Assign(
                targets=[node.target],
                value=Call(
                    func=Name(id=op_name, ctx=Load()),
                    args=[left, right],
                    keywords=[],
                ),
            )
        )
        self._symbol_update(*new_node.operator_import_symbols)
        return new_node.result

    def visit_BinOp(self, node: BinOp) -> Call:
        left, right = node.left, node.right
        op_name = get_bin_conversion(get_cls_name_of(node.op))
        self._symbol_update(op_name)
        new_node = OperationNodeTransformer(
            Call(
                func=Name(id=op_name, ctx=Load()),
                args=[left, right],
                keywords=[],
            )
        )
        self._symbol_update(*new_node.operator_import_symbols)
        return new_node.result

    def visit_Compare(self, node: Compare) -> Call:
        flat = [node.left] + node.comparators
        new_comparators = []
        for current, next, cmp_ops in zip(flat, flat[1:], node.ops):
            cmp_name = get_cmp_conversion(get_cls_name_of(cmp_ops))
            self._symbol_update(cmp_name)
            new_comparators.append(
                Call(
                    func=Name(id=cmp_name, ctx=Load()),
                    args=[current, next],
                    keywords=[],
                )
            )
        new_node = OperationNodeTransformer(BoolOp(op=And(), values=new_comparators))
        self._symbol_update(*new_node.operator_import_symbols)
        return new_node.result
"""
