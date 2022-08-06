from abc import ABC, abstractmethod
from ast import AST, Assign, AugAssign, BinOp, Call, Compare, NodeTransformer
from typing import Any, Iterable


class AbstractBaseStandardOperationFunctionNodeTransformer(ABC, NodeTransformer):
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

    @abstractmethod
    def visit_Compare(self, node: Compare) -> Call:
        """
        Abstract method to implement `Compare` to `Call` conversion on a node

        Args:
            node (Compare): Compare node

        Returns:
            Call: Call node after conversion to operator function equivalent

        Example:
            Initial:
                x, y = 1, 2
                print(y > x)

            Conversion:
                from operator import ge
                x, y = 1, 2
                print(ge(x, y))
        """

    @abstractmethod
    def _extend_import_symbols(self, *import_symbols: str) -> None:
        """
        Private abstract method to report use of an `operator` function, as such they can be
        imported for use when the tree gets finalized.

        Args:
            import_symbols (str): str instances which are import symbols
                                  which are meant to be imported from stdlib operator
        """
        ...

    @property
    @abstractmethod
    def operator_import_symbols(self) -> Iterable[str]:
        """
        Abstract property which returns an iterable of str instances which are
        reported to be used as import symbols

        Returns:
            Iterable[str]: Import symbols from stdlib operator
        """

    @property
    @abstractmethod
    def result(self) -> Any:  # TODO: This can may be narrowed?
        """
        Abstract property which returns abstract syntax tree node where appropriate
        conversions have taken place, nodes returned by this decriptor can be expected to
        have non-missing `lineno` and `col_offset`

        Returns:
            AST: Abstract Syntax Tree
        """
