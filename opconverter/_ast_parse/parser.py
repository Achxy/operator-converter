from ast import fix_missing_locations
from .operators import OperationNodeTransformer
from .attr import AttributeManipulationTransformer
from typing import Any
from collections.abc import Iterable


class Foo(OperationNodeTransformer, AttributeManipulationTransformer):
    def __init__(self, tree) -> None:
        self._operator_import_sym: set[str] = set()
        self._result = fix_missing_locations(self.visit(tree))

    def _extend_import_symbols(self, *import_symbols: str) -> None:
        self._operator_import_sym.update(import_symbols)

    @property
    def operator_import_symbols(self) -> Iterable[str]:
        return self._operator_import_sym

    @property
    def result(self) -> Any:
        return self._result
