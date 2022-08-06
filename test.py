from opconverter._ast_parse.parser import Foo

sample = """\
def foo(a, b):
    return a + b
"""
from ast import parse, dump, unparse

print(unparse(Foo(parse(sample)).result))
