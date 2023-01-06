"""
A logical operator is a symbol or word used to connect two or more expressions
such that the value of the compound expression produced depends only on that of the original
expressions and on the meaning of the operator. Common logical operators include AND, OR, and NOT.

Logical operator & Meaning

and -->	( expression1 and expression2 ) true only if both expression1 and expression2 are true
or -->	( expression1 or expression2 ) true if either expression1 or expression2 is true
not -->	not( expression ) true if expression is false
"""
# Logical Operators in Python
"""
and
or
not
"""
a = 25
print(a >= 10 and a <= 20)
print(a >= 10 or a <= 20)
print(not(a >=  10 and a <= 20))