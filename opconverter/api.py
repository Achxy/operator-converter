from .ast_parse import StandardOperationFunctionNodeTransformer
from .ast_parse.import_helper import add_ImportFromNode
from ast import parse, unparse


def convert_operations(pycode: str, make_imports: bool = True) -> str:
    tree = parse(pycode)
    new = StandardOperationFunctionNodeTransformer(tree)
    if make_imports:
        add_ImportFromNode(new.result, "operator", new.operator_import_symbols)
    return unparse(new.result)
