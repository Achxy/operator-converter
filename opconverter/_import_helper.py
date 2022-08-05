from typing import Final, Iterable
from ast import Module, ImportFrom, alias

FUTURE_IMPORT: Final[str] = "__future__"


def _is_ImportFromFuture(node) -> bool:
    return isinstance(node, ImportFrom) and node.module == FUTURE_IMPORT


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
