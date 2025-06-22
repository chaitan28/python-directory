import sys

def add(a, b):
    c = a + b
    return f"Addition: {c}"

def sub(a, b):
    d = a - b
    return f"Subtraction: {d}"

def multiply(a, b):
    e = a * b
    return f"Multiplication: {e}"

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    f = a / b
    return f"Division: {f}"

def remainder(a, b):
    h = a % b
    return f"Remainder: {h}"

# Input handling
a = float(sys.argv[1])
operation = sys.argv[2]
b = float(sys.argv[3])

# Operation execution
if operation == "add":
    print(add(a, b))
elif operation == "sub":
    print(sub(a, b))
elif operation == "multiply":
    print(multiply(a, b))
elif operation == "divide":
    print(divide(a, b))
elif operation == "remainder":
    print(remainder(a, b))
else:
    print("Unsupported operation. Use add, sub, multiply, divide, or remainder.")
