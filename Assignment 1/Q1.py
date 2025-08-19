# Write a Python program to swap two variables using a temporary variable andwithout using a temporary variable

x = 15
y = 20

print("Before swap (without temp): x =", x, "y =", y)
x, y = y, x
print("After swap (without temp): x =", x, "y =", y)