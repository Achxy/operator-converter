from abc import ABC, abstractmethod
from ast import Assign, NodeTransformer, AugAssign, BinOp, Call


class AbstractStandardOperationFunctionTransformer(ABC, NodeTransformer):
    __slots__ = ()

    @abstractmethod
    def visit_AugAssign(self, node: AugAssign) -> Assign:
        """
        Abstract method to implement `AugAssign` to `Assign` conversion on a node

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

    @abstractmethod
    def visit_BinOp(self, node: BinOp) -> Call:
        """
        Abstract method to implement `BinOp` to `Call` conversion on a node

        Args:
            node (BinOp): BinOp node

        Returns:
            Call: Call node after conversion to operator function equivalent

        Example:
            Initial:
                a, b = 1, 2
                c = a + b
                print(c)
            Conversion:
                from operator import add
                a, b = 1, 2
                c = add(a, b)
                print(C)
        """
