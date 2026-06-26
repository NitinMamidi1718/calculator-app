def cube(a):
    return a * a * a
def add(a, b):
    return a + b

def square(number):
    return number * number

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
def power(base, exponent):
    x = base ** exponent
    y = x
    return y
def average(a, b):
    return (a + b) / 2

print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))