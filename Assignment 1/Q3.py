# Write a program to calculate the factorial of a number using a loop.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = 5
print("Factorial of", num, "is", factorial(num))