

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def main():
    print("=== Simple Calculator ===")
    print("Addition (5 + 3):", add(5, 3))
    print("Subtraction (10 - 2):", subtract(10, 2))
    print("Multiplication (4 * 6):", multiply(4, 6))
    print("Division (8 / 2):", divide(8, 2))

if __name__ == "__main__":
    main()
