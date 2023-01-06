"""
In Python, bitwise operators are used to perform bitwise calculations on integers.
The integers are first converted into binary and then operations are performed on bit by bit, hence the name bitwise operators.
 Then the result is returned in decimal format.
Bitwise AND operator: Returns 1 if both the bits are 1 else 0
"""
"""
& 	AND
|	OR
^	XOR
~ 	NOT
<<	Zero fill left shift
>>	Signed right shift
"""
a = 25
b = 45
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 2)
print(a >> 2)