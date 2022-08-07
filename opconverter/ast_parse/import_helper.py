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
from ast import ImportFrom, Module, alias
from typing import Iterable

from ._constants import DUNDER_FUTURE_IMPORT


def _is_ImportFromFuture(node) -> bool:
    return isinstance(node, ImportFrom) and node.module == DUNDER_FUTURE_IMPORT


def add_ImportFromNode(
    mod: Module, mod_name: str, symbols: Iterable[str], level: int = 0
) -> None:
    node = ImportFrom(
        module=mod_name,
        names=[alias(name=name) for name in symbols],
        level=level,
    )
    body = mod.body
    first_expr = body[0]
    body.insert(int(_is_ImportFromFuture(first_expr)), node)
