import math

# Function to handle basic arithmetic operations
def perform_operation(left, operator, right):
    if operator == "+":
        return left + right
    elif operator == "-":
        return left - right
    elif operator == "*":
        return left * right
    elif operator == "/":
        return left / right
    elif operator == "^":
        return left ** right
    else:
        raise ValueError(f"Unsupported operator: {operator}")

# Function to evaluate a list of tokens (numbers and operators)
def evaluate_tokens(tokens):
    while "^" in tokens:
        index = tokens.index("^")
        tokens[index-1] = perform_operation(float(tokens[index-1]), tokens[index], float(tokens[index+1]))
        del tokens[index:index+2]

    while "*" in tokens or "/" in tokens:
        for operator in ["*", "/"]:
            if operator in tokens:
                index = tokens.index(operator)
                tokens[index-1] = perform_operation(float(tokens[index-1]), tokens[index], float(tokens[index+1]))
                del tokens[index:index+2]
                break

    while "+" in tokens or "-" in tokens:
        for operator in ["+", "-"]:
            if operator in tokens:
                index = tokens.index(operator)
                tokens[index-1] = perform_operation(float(tokens[index-1]), tokens[index], float(tokens[index+1]))
                del tokens[index:index+2]
                break

    return tokens[0]

# Function to solve the mathematical problem
def solve(problem):
    problem = problem.replace("(", " ( ").replace(")", " ) ").replace("^", " ^ ")
    tokens = problem.split()
    
    def evaluate_parentheses(tokens):
        start = tokens.rindex("(")
        end = tokens.index(")", start)
        tokens[start:end+1] = [evaluate_tokens(tokens[start+1:end])]
        return tokens

    while "(" in tokens:
        tokens = evaluate_parentheses(tokens)

    return evaluate_tokens(tokens)

def main():
    print("Make sure to use ' ' to separate operators, brackets, and numbers.")
    print("Use * for multiplication, / for division, ^ for powers, sqrt for square root, and pi for Pi")
    problem = input("Enter math problem: \n")
    try:
        result = solve(problem)
        print(f"{problem} = {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
