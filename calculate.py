from sympy import sympify
import numpy as np
import sys

def calculate(expression: str):
    try:
        sym_expression = sympify(expression)
        return sym_expression
    except Exception as e:
        return f"Error in calculation: {e}"


if __name__ == '__main__':
    print(calculate(sys.argv[1]))

# Evaluating a simple expression
#expression_string = "x**2 - 4"
#x = Symbol('x')
#sym_expression = sympify(expression_string)
#solutions = solve(sym_expression, x)
#print(f"The solutions for '{expression_string}' are: {solutions}")

# Substituting values into an expression
#n = Symbol('n')
#equation_with_variable = "23 / (n + 2)"
#sym_equation = sympify(equation_with_variable)

#for i in range(3):
#    evaluated_value = sym_equation.subs({n: i}).evalf()
#    print(f"When n = {i}, the value of '{equation_with_variable}' is: {evaluated_value}")