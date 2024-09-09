def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def print_operations(a, b):
    print(f"sum = {add(a, b)}, diff = {subtract(a, b)}, prod = {multiply(a, b)}, div = {divide(a, b)}, mod = {modulus(a, b)}, pow = {power(a, b)}")


num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))

print_operations(num1, num2)
