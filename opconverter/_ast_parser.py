from ast import (
    And,
    Assign,
    BinOp,
    BoolOp,
    Call,
    Load,
    Module,
    Name,
    NodeTransformer,
    fix_missing_locations,
    parse,
    Compare,
    AugAssign,
    unparse,
)


class OperationNodeTransformer(NodeTransformer):
    def __init__(self, tree) -> None:
        self.operator_import_symbols: set[str] = set()
        self.result = fix_missing_locations(self.visit(tree))

    def _symbol_update(self, *import_symbol: str) -> None:
        self.operator_import_symbols.update(import_symbol)


def convert_operations(py_code: str) -> str:
    tree: Module = parse(py_code)
    new = OperationNodeTransformer(tree)
    add_ImportFromNode(new.result, "operator", new.operator_import_symbols)
    return unparse(new.result)
