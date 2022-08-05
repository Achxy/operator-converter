from abc import ABC, abstractmethod
from ast import Assign, NodeTransformer, AugAssign


class AbstractStandardOperationFunctionTransformer(ABC, NodeTransformer):
    __slots__ = ()

    @abstractmethod
    def visit_AugAssign(self, node: AugAssign) -> Assign:
        """
        Abstract method to implement Augmented Assignments on a node

        Args:
            node (AugAssign): AugAssign node

        Returns:
            Assign: Assign node after conversion to operator function equivalent

        Example:
            Initial:
                a = 0
                a += 1

            Conversion:
                from operator import iadd
                a = 0
                a = iadd(a, 1)
        """
