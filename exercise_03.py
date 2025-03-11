# Russell Togno
# ITELEC2
# Laboratory #05 – Arithmetic Operators and Operator Precedence in Python

# Define numeric variables
a = 10
b = 5
c = 3

# Calculate expressions demonstrating operator precedence
result1 = a + b * c  # Multiplication (*) happens before addition (+)
print("Result of a + b * c:", result1)

# Using parentheses to change precedence
result2 = (a + b) * c  # Addition inside parentheses happens first
print("Result of (a + b) * c:", result2)

# Subtraction operation
result3 = a - b
print("Result of a - b:", result3)

# Standard and floor division
result4 = a / b  # Division (/) results in a float
result5 = a // b  # Floor division (//) results in an integer
print("Result of a / b:", result4)
print("Result of a // b (floor division):", result5)

# Modulus and exponentiation operations
result6 = a % b  # Modulus (%) returns the remainder
result7 = a ** c  # Exponentiation (**) raises 'a' to the power of 'c'
print("Result of a % b (modulus):", result6)
print("Result of a ** c (exponentiation):", result7)

# Complex expression combining multiple operators
result8 = (a + b - c) * (a / b)
print("Result of (a + b - c) * (a / b):", result8)
