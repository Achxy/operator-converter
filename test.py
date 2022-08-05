from ast import dump, parse
from opconverter import convert_operations

print(dump(parse("a += 1"), indent=4))
print(convert_operations("a += 1"))
