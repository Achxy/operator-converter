"""
ConvertOperator is a project for converting standard operations to functions
Copyright (C) 2022-present  Achxy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
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
