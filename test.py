from ast import dump, parse
from opconverter._ast_parser import convert_operations


print(dump(parse("1 > 2 > 3 > 4"), indent=4))
print(6 < 6 >= 6 > 4)
print(dump(parse("x in y in z"), indent=4))
print(dump(parse("x or y or z"), indent=4))

print(convert_operations("1 > 2 > 3 > 4"))
