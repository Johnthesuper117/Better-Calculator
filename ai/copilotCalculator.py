import math

# Define basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Define advanced mathematical functions
def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x, base=math.e):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Define a function to evaluate expressions
def evaluate_expression(expression):
    # Replace mathematical functions with their corresponding function calls
    expression = expression.replace('^', '**')
    expression = expression.replace('sqrt', 'math.sqrt')
    expression = expression.replace('log', 'math.log')
    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')
    expression = expression.replace('tan', 'math.tan')
    
    # Evaluate the expression
    try:
        result = eval(expression)
    except Exception as e:
        return f"Error: {e}"
    return result

# User interface
def calculator():
    print("Advanced Python Calculator")
    print("Supported operations: +, -, *, /, ^ (power)")
    print("Supported functions: sqrt(x), log(x, base), sin(x), cos(x), tan(x)")
    
    while True:
        expression = input("Enter expression (or type 'quit' to exit): ")
        if expression.lower() == 'quit':
            break
        result = evaluate_expression(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
