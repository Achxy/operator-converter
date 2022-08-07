from opconverter import convert_operations

sample = """\
def foo(a, b, c):
    b += c
    return ~(a + b)
"""

print(convert_operations(sample))
