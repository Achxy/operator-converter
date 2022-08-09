# [ConvertOperator](https://github.com/Achxy/ConvertOperator/tree/main)

A source converter made for fun based off [this question](https://stackoverflow.com/questions/73246025/) on StackOverflow

# Examples
Quick examples to demonstrate working of this project :

Before conversion:
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(5))
```
After conversion:
```python
from operator import sub, add, le

def fib(n):
    if le(n, 1):
        return n
    return add(fib(sub(n, 1)), fib(sub(n, 2)))

print(fib(5))
```
## ---
Before conversion:
```python
def foo(x, y, z):
    z += 1
    y = x >> y
    x @= y
    x, y = y, x
    return (x + y ^ z) or y // x
```
After conversion:
```python
from operator import xor, imatmul, iadd, rshift, add, floordiv

def foo(x, y, z):
    z = iadd(z, 1)
    y = rshift(x, y)
    x = imatmul(x, y)
    (x, y) = (y, x)
    return xor(add(x, y), z) or floordiv(y, x)
```

# Features
The following conversions are implemented :

1. [Unary Operations](https://docs.python.org/3/library/ast.html#ast.UnaryOp)
1. [Binary Operations](https://docs.python.org/3/library/ast.html#ast.BinOp)
1. [Comparsion Operators](https://docs.python.org/3/library/ast.html#ast.Compare)
1. [Subscript Operations](https://docs.python.org/3/library/ast.html#ast.Subscript) [❌TODO]
1. [Augmented Assignmented Operations](https://docs.python.org/3/library/ast.html#ast.AugAssign)
