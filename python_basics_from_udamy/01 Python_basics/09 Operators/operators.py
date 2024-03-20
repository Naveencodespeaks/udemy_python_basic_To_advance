"""
python supports various operators, which are symbols that carry out operations on operands. Here's an overview of the different types of operators in Python:

Arithmetic Operators:

Addition: +
Subtraction: -
Multiplication: *
Division: /
Floor Division: // (division that results in the whole number adjusted to the left in the number line)
Modulus (Remainder): %
Exponentiation: **
Comparison (Relational) Operators:

Equal to: ==
Not equal to: !=
Greater than: >
Less than: <
Greater than or equal to: >=
Less than or equal to: <=
Assignment Operators:

Assign value: =
Add and assign: +=
Subtract and assign: -=
Multiply and assign: *=
Divide and assign: /=
Floor divide and assign: //=
Modulus and assign: %=
Exponentiate and assign: **=
Logical Operators:

Logical AND: and
Logical OR: or
Logical NOT: not
Bitwise Operators:

Bitwise AND: &
Bitwise OR: |
Bitwise XOR: ^
Bitwise NOT: ~
Left shift: <<
Right shift: >>
Membership Operators:

in: Evaluates to True if a sequence (list, tuple, or string) contains a specified value.
not in: Evaluates to True if a sequence does not contain a specified value.
Identity Operators:

is: Evaluates to True if both variables point to the same object.
is not: Evaluates to True if both variables do not point to the same object.
Unary Operators:

Unary positive: +x
Unary negative: -x
"""

print(10 + 20)
print(10 - 20)
print(20 * 3)
print(10 / 2 )
print(10 // 3)
print(50 ** 2)
a = 5
b = 10
a = a + 3
a +=3
a -= 3
a *= 3
a /= 3
a //= 3
a **= 3
print(a)
print(10 == 10)
print( 10 > 10)
print(20 < 10)
print(10 != 5)
print( 30>= 30)
print( 10 <= 40)
print( 20 > 10)
print( 20 < 7)
a = 5
b = 10

print(a < b and 4 > 6 )
print(a < b or 4 > 6 )
print(not(a < b or 4 > 6 ))
print(not(a < b or 4 > 6 ))

# Identiti operator
a = 100.0
b = 1.0 * a
print(id(a))
print(id(b))

print(a is b)
print( a == b)
print(a is not b)

numbers = [1,2,3,4,5,6]
print(1 in numbers)
print(10 in numbers)
print(6 in numbers)