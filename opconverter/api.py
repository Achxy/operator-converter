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
from ast import parse, unparse

from .ast_parse import StandardOperationFunctionNodeTransformer
from .ast_parse.import_helper import add_ImportFromNode


def convert_operations(pycode: str, make_imports: bool = True) -> str:
    tree = parse(pycode)
    new = StandardOperationFunctionNodeTransformer(tree)
    if make_imports:
        add_ImportFromNode(new.result, "operator", new.operator_import_symbols)
    return unparse(new.result)
