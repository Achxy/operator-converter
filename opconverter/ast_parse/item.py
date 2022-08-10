from ast import Assign, Call, Del, Load, Name, Store, Subscript

from .abstract import AbstractBaseStandardOperationFunctionNodeTransformer
from ._helpers import Function
from ._constants import OPERATOR_GETITEM, OPERATOR_DELITEM

# FIXME: Subscript nodes with Del as ctx are always wrapper in ast.Delete node
# Direct modification will lead to the function being in place of the delete context
# This has to be fixed
# FIXME: This does not update import symbols
class ItemManipulationTransformer(AbstractBaseStandardOperationFunctionNodeTransformer):
    __slots__ = ()

    def visit_Subscript(self, node: Subscript):
        ctx = node.ctx
        if isinstance(ctx, Load):
            return self._get_subscript(node)
        elif isinstance(ctx, Del):
            return self._del_subscript(node)

    def _get_subscript(self, node: Subscript):
        return Function(OPERATOR_GETITEM, node.value, node.slice)

    def _set_subscript(self, obj, target, value):  # ambiguous
        pass

    def _del_subscript(self, node):
        return Function(OPERATOR_DELITEM, node.value, node.slice)
