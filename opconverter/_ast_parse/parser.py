from ast import AST, fix_missing_locations
from collections.abc import Iterable
from typing import Any

from .attr import AttributeManipulationTransformer
from .operators import OperationNodeTransformer


class StandardOperationFunctionNodeTransformer(
    OperationNodeTransformer, AttributeManipulationTransformer
):
    __slots__ = ("_operator_import_sym", "_result")

    def __init__(self, node: AST) -> None:
        self._operator_import_sym: set[str] = set()
        self._result = fix_missing_locations(self.visit(node))

    def _extend_import_symbols(self, *import_symbols: str) -> None:
        self._operator_import_sym.update(import_symbols)

    @property
    def operator_import_symbols(self) -> Iterable[str]:
        return self._operator_import_sym

    @property
    def result(self) -> Any:
        return self._result
