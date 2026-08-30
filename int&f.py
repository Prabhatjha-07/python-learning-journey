# num = 5 
# print(type(num)) - prints the type of the variable 

# print(abs(-5)) - prints the absolute value of the number

# from math import floor, ceil


# print(round(5.6)) - rounds the number to the nearest integer
# print(floor(5.6)) - rounds the number down to the nearest integer
# print(ceil(5.6)) - rounds the number up to the nearest integer
# print(round(5.455, 2)) - rounds the number to the nearest integer with 2 decimal places

from math import remainder
import numbers


num1 = 3 
num2 = 2 

hel = '3'


hel = int(hel) - converts the string to an integer
hel = float(hel) - converts the string to a float
hel = str(hel) - converts the float to a string
hel = bool(hel) - converts the string to a boolean value
hel = complex(hel) - converts the string to a complex number
hel = list(hel) - converts the string to a list
hel = tuple(hel) - converts the string to a tuple
hel = set(hel) - converts the string to a set
hel = dict(hel) - converts the string to a dictionary
hel = bytes(hel) - converts the string to a bytes object
hel = bytearray(hel) - converts the string to a bytearray object
hel = memoryview(hel) - converts the string to a memoryview object
hel = frozenset(hel) - converts the string to a frozenset object
hel = range(hel) - converts the string to a range object

| Conversion                | What it does                                                                                                | Example                           | Output                            |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------- | --------------------------------- |
| `int(hel)`                | Converts a numeric string to an integer.                                                                    | `int("25")`                       | `25`                              |
| `float(hel)`              | Converts a numeric string to a floating-point number.                                                       | `float("25.5")`                   | `25.5`                            |
| `str(hel)`                | Converts any object to a string.                                                                            | `str(25)`                         | `"25"`                            |
| `bool(hel)`               | Converts a value to a Boolean (`True` or `False`). Non-empty strings are `True`; empty strings are `False`. | `bool("")`                        | `False`                           |
| `complex(hel)`            | Converts a number or numeric string to a complex number.                                                    | `complex("5")`                    | `(5+0j)`                          |
| `list(hel)`               | Converts an iterable into a list. A string becomes a list of characters.                                    | `list("abc")`                     | `['a', 'b', 'c']`                 |
| `tuple(hel)`              | Converts an iterable into a tuple.                                                                          | `tuple("abc")`                    | `('a', 'b', 'c')`                 |
| `set(hel)`                | Converts an iterable into a set (removes duplicates).                                                       | `set("hello")`                    | `{'h', 'e', 'l', 'o'}`            |
| `dict(hel)`               | Converts key-value pairs into a dictionary. **Does not work on a normal string.**                           | `dict([('a',1), ('b',2)])`        | `{'a': 1, 'b': 2}`                |
| `bytes(hel, "utf-8")`     | Converts a string to a bytes object using an encoding.                                                      | `bytes("Hi", "utf-8")`            | `b'Hi'`                           |
| `bytearray(hel, "utf-8")` | Converts a string to a mutable byte array.                                                                  | `bytearray("Hi", "utf-8")`        | `bytearray(b'Hi')`                |
| `memoryview(hel)`         | Creates a memory view of a bytes-like object. **Cannot use a string directly.**                             | `memoryview(bytes("Hi","utf-8"))` | `<memory at ...>`                 |
| `frozenset(hel)`          | Converts an iterable into an immutable set.                                                                 | `frozenset("hello")`              | `frozenset({'h', 'e', 'l', 'o'})` |
| `range(hel)`              | Creates a range of numbers. **Requires an integer, not a string.**                                          | `range(5)`                        | `range(0, 5)`                     |


# difference between list, tuple, set and dictionary

| Feature              | List (`[]`)      | Tuple (`()`)     | Set (`{}`)         | Dictionary (`{key: value}`) |
| -------------------- | ---------------- | ---------------- | ------------------ | --------------------------- |
| Syntax               | `[]`             | `()`             | `{}`               | `{key: value}`              |
| Ordered              | ✅ Yes            | ✅ Yes            | ❌ No               | ✅ Yes (Python 3.7+)         |
| Mutable (can change) | ✅ Yes            | ❌ No             | ✅ Yes              | ✅ Yes                       |
| Allows duplicates    | ✅ Yes            | ✅ Yes            | ❌ No               | Keys: ❌ No, Values: ✅ Yes   |
| Indexed              | ✅ Yes            | ✅ Yes            | ❌ No               | Access by key               |
| Main purpose         | Store a sequence | Store fixed data | Store unique items | Store key-value pairs       |



print(num1 + num2) - prints the sum of the two numbers
print(num1 - num2) - prints the difference of the two numbers
print(num1 * num2) - prints the product of the two numbers
print(num1 / num2) - prints the quotient of the two numbers
print(num1 // num2) - prints the quotient of the two numbers without the decimal part
print(num1 % num2) - prints the remainder of the two numbers
print(num1 ** num2) - prints the result of raising the first number to the power of the second number
print(pow(num1, num2)) - prints the result of raising the first number to the power of the second number
print(divmod(num1, num2)) - returns a tuple of quotient and remainder
print(remainder(num1, num2)) - returns the remainder of the two numbers
print(numbers.isclose(num1, num2)) - returns True if the two numbers are close to each other within a certain tolerance
print(numbers.isfinite(num1)) - returns True if the number is finite
print(numbers.isinf(num1)) - returns True if the number is infinite
print(numbers.isnan(num1)) - returns True if the number is NaN (not a number)
print(numbers.isqrt(num1)) - returns the integer square root of the number
print(numbers.gcd(num1, num2)) - returns the greatest common divisor of the two numbers
print(numbers.lcm(num1, num2)) - returns the least common multiple of the two numbers
print(numbers.factorial(num1)) - returns the factorial of the number
print(numbers.perm(num1, num2)) - returns the number of permutations of num1 taken num2 at a time
print(numbers.comb(num1, num2)) - returns the number of combinations of num1 taken num2 at a time
print(numbers.prod([num1, num2])) - returns the product of the numbers in the iterable
print(numbers.fsum([num1, num2])) - returns the sum of the numbers in the iterable


| Function                     | What it does                                                                                                              | Example                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `divmod(num1, num2)`         | Returns **both quotient and remainder** as a tuple `(quotient, remainder)`.                                               | `divmod(10, 3)` → `(3, 1)`                                                     |
| `math.remainder(num1, num2)` | Returns the IEEE 754 floating-point remainder. This is **different from `%`**.                                            | `math.remainder(10, 3)` → `1.0`                                                |
| `math.isclose(num1, num2)`   | Checks whether two numbers are approximately equal within a small tolerance. Useful for comparing floating-point numbers. | `math.isclose(0.1+0.2, 0.3)` → `True`                                          |
| `math.isfinite(num1)`        | Returns `True` if the number is neither infinity nor NaN.                                                                 | `math.isfinite(5)` → `True`                                                    |
| `math.isinf(num1)`           | Returns `True` if the number is positive or negative infinity.                                                            | `math.isinf(float('inf'))` → `True`                                            |
| `math.isnan(num1)`           | Returns `True` if the value is NaN ("Not a Number").                                                                      | `math.isnan(float('nan'))` → `True`                                            |
| `math.isqrt(num1)`           | Returns the integer (floor) square root.                                                                                  | `math.isqrt(17)` → `4`                                                         |
| `math.gcd(num1, num2)`       | Returns the Greatest Common Divisor (GCD).                                                                                | `math.gcd(12, 18)` → `6`                                                       |
| `math.lcm(num1, num2)`       | Returns the Least Common Multiple (LCM).                                                                                  | `math.lcm(12, 18)` → `36`                                                      |
| `math.factorial(num1)`       | Returns the factorial (`n!`).                                                                                             | `math.factorial(5)` → `120`                                                    |
| `math.perm(num1, num2)`      | Returns the number of permutations: **nPr** = `n! / (n-r)!`.                                                              | `math.perm(5, 2)` → `20`                                                       |
| `math.comb(num1, num2)`      | Returns the number of combinations: **nCr** = `n! / (r!(n-r)!)`.                                                          | `math.comb(5, 2)` → `10`                                                       |
| `math.prod([num1, num2])`    | Multiplies all elements in an iterable.                                                                                   | `math.prod([4, 5])` → `20`                                                     |
| `math.fsum([num1, num2])`    | Returns an accurate floating-point sum, reducing rounding errors.                                                         | `math.fsum([0.1, 0.2])` → `0.30000000000000004` (more accurate for long lists) |




| Operator | Meaning                                                        | Example              | Result            |
| -------- | -------------------------------------------------------------- | -------------------- | ----------------- |
| `==`     | Equal to                                                       | `10 == 10`           | `True`            |
| `!=`     | Not equal to                                                   | `10 != 5`            | `True`            |
| `>`      | Greater than                                                   | `10 > 5`             | `True`            |
| `<`      | Less than                                                      | `10 < 5`             | `False`           |
| `>=`     | Greater than or equal to                                       | `10 >= 10`           | `True`            |
| `<=`     | Less than or equal to                                          | `10 <= 5`            | `False`           |
| `is`     | Checks if two variables refer to the **same object** in memory | `a is b`             | `True` or `False` |
| `is not` | Checks if two variables refer to **different objects**         | `a is not b`         | `True` or `False` |
| `in`     | Checks if a value exists in a sequence                         | `'a' in "apple"`     | `True`            |
| `not in` | Checks if a value does **not** exist in a sequence             | `'z' not in "apple"` | `True`            |


