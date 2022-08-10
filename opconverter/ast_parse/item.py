from ast import Assign, Call, Del, Load, Name, Store, Subscript

from .abstract import AbstractBaseStandardOperationFunctionNodeTransformer


class ItemManipulationTransformer(AbstractBaseStandardOperationFunctionNodeTransformer):
    __slots__ = ()

    def visit_Subscript(self, node: Subscript):
        ctx = node.ctx
        if isinstance(ctx, Load):
            return self._get_subscript(node)
        elif isinstance(ctx, Del):
            return self._del_subscript(node)

    def _get_subscript(self, node: Subscript):
        return Call(
            func=Name(id="getitem", ctx=Load()),
            args=[node.value, node.slice],
            keywords=[],
        )

    def _set_subscript(self, obj, target, value):  # ambiguous
        pass

    def _del_subscript(self, node):
        return Call(
            func=Name(id="delitem", ctx=Load()),
            args=[node.value, node.slice],
            keywords=[],
        )
