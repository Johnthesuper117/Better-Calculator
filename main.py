import math
#supports low level algebra
#Notes:
#Decimals don't work
#Fractions not included
#Can't solve for variables
def solve(problem):
    problemList = problem.split()
    print(problemList)
    if problemList.count("(") != 0:
        ii = problemList.count("(")
        while ii > 0:
            print("There are " + str(problemList.count("(")) + " (")
            print("There are " + str(problemList.count(")")) + " )")
            stringProblemList = "".join(problemList)
            print(stringProblemList)
            print(stringProblemList.rindex("("))
            leftBracket = stringProblemList.rindex("(")
            rightBracket = problemList.index(")")
            brackeList = problemList[leftBracket+1:rightBracket]
            print("bracket list: ", brackeList)
            if brackeList.count("pi") != 0:
                i = brackeList.count("pi")
                while i > 0:
                    print("There are " + str(brackeList.count("pi")) + " pi")
                    solution = math.pi
                    brackeList[brackeList.index("pi")] = str(solution)
                    print(brackeList)
                    i -= 1
            if brackeList.count("^") != 0:
                i = brackeList.count("^")
                while i > 0:
                    print("There are " + str(brackeList.count("^")) + " ^")
                    solution = int(brackeList[brackeList.index("^")-1]) ** int(brackeList[brackeList.index("^")+1])
                    del brackeList[brackeList.index("^")-1]
                    del brackeList[brackeList.index("^")+1]
                    brackeList[brackeList.index("^")] = str(solution)
                    print(brackeList)
                    i -= 1
            if brackeList.count("sqrt") != 0:
                i = brackeList.count("sqrt")
                while i > 0:
                    print("There are " + str(brackeList.count("sqrt")) + " sqrt")
                    solution = math.sqrt(int(brackeList[brackeList.index("sqrt")+1]))
                    del brackeList[brackeList.index("sqrt")+1]
                    brackeList[brackeList.index("sqrt")] = str(solution)
                    print(brackeList)
                    i -= 1
            if brackeList.count("*") != 0:
                i = brackeList.count("*")
                while i > 0:
                    print("There are " + str(brackeList.count("*")) + " *")
                    solution = int(brackeList[brackeList.index("*")-1]) * int(brackeList[brackeList.index("*")+1])
                    del brackeList[brackeList.index("*")-1]
                    del brackeList[brackeList.index("*")+1]
                    brackeList[brackeList.index("*")] = str(solution)
                    print(brackeList)
                    i -= 1
            if brackeList.count("/") != 0:
                i = brackeList.count("/")
                while i > 0:
                    print("There are " + str(brackeList.count("/")) + " /")
                    solution = int(brackeList[brackeList.index("/")-1]) / int(brackeList[brackeList.index("/")+1])
                    del brackeList[brackeList.index("/")-1]
                    del brackeList[brackeList.index("/")+1]
                    brackeList[brackeList.index("/")] = str(solution)
                    print(brackeList)
                    i -= 1
            if brackeList.count("+") != 0:
                i = brackeList.count("+")
                while i > 0:
                    print("There are " + str(brackeList.count("+")) + " +")
                    solution = int(brackeList[brackeList.index("+")-1]) + int(brackeList[brackeList.index("+")+1])
                    del brackeList[brackeList.index("+")-1]
                    del brackeList[brackeList.index("+")+1]
                    brackeList[brackeList.index("+")] = str(solution)
                    print(brackeList)
                    i -= 1
            if brackeList.count("-") != 0:
                i = brackeList.count("-")
                while i > 0:
                    print("There are " + str(brackeList.count("-")) + " -")
                    solution = int(brackeList[brackeList.index("-")-1]) - int(brackeList[brackeList.index("-")+1])
                    del brackeList[brackeList.index("-")-1]
                    del brackeList[brackeList.index("-")+1]
                    brackeList[brackeList.index("-")] = str(solution)
                    print(brackeList)
                    i -= 1
            del problemList[leftBracket+1:rightBracket]
            del problemList[problemList.index(")")]
            problemList[stringProblemList.rindex("(")] = str(solution)
            print(problemList)
            ii -= 1
    if problemList.count("pi") != 0:
        i = problemList.count("pi")
        while i > 0:
            print("There are " + str(problemList.count("pi")) + " pi")
            solution = math.pi
            problemList[problemList.index("pi")] = str(solution)
            print(problemList)
            i -= 1
    if problemList.count("^") != 0:
        i = problemList.count("^")
        while i > 0:
            print("There are " + str(problemList.count("^")) + " ^")
            solution = int(problemList[problemList.index("^")-1]) ** int(problemList[problemList.index("^")+1])
            del problemList[problemList.index("^")-1]
            del problemList[problemList.index("^")+1]
            problemList[problemList.index("^")] = str(solution)
            print(problemList)
            i -= 1
    if problemList.count("sqrt") != 0:
        i = problemList.count("sqrt")
        while i > 0:
            print("There are " + str(problemList.count("sqrt")) + " sqrt")
            solution = math.sqrt(int(problemList[problemList.index("sqrt")+1]))
            del problemList[problemList.index("sqrt")+1]
            problemList[problemList.index("sqrt")] = str(solution)
            print(problemList)
            i -= 1
    if problemList.count("*") != 0:
        i = problemList.count("*")
        while i > 0:
            print("There are " + str(problemList.count("*")) + " *")
            solution = int(problemList[problemList.index("*")-1]) * int(problemList[problemList.index("*")+1])
            del problemList[problemList.index("*")-1]
            del problemList[problemList.index("*")+1]
            problemList[problemList.index("*")] = str(solution)
            print(problemList)
            i -= 1
    if problemList.count("/") != 0:
        i = problemList.count("/")
        while i > 0:
            print("There are " + str(problemList.count("/")) + " /")
            solution = int(problemList[problemList.index("/")-1]) / int(problemList[problemList.index("/")+1])
            del problemList[problemList.index("/")-1]
            del problemList[problemList.index("/")+1]
            problemList[problemList.index("/")] = str(solution)
            print(problemList)
            i -= 1
    if problemList.count("+") != 0:
        i = problemList.count("+")
        while i > 0:
            print("There are " + str(problemList.count("+")) + " +")
            solution = int(problemList[problemList.index("+")-1]) + int(problemList[problemList.index("+")+1])
            del problemList[problemList.index("+")-1]
            del problemList[problemList.index("+")+1]
            problemList[problemList.index("+")] = str(solution)
            print(problemList)
            i -= 1
    if problemList.count("-") != 0:
        i = problemList.count("-")
        while i > 0:
            print("There are " + str(problemList.count("-")) + " -")
            solution = int(problemList[problemList.index("-")-1]) - int(problemList[problemList.index("-")+1])
            del problemList[problemList.index("-")-1]
            del problemList[problemList.index("-")+1]
            problemList[problemList.index("-")] = str(solution)
            print(problemList)
            i -= 1
    return solution
print("Make sure to use ' ' to separate operators, brackets, and numbers. Use * for multiplication, / for division, ^ for powers, sqrt for square root and pi for Pi")    
problem = input("Enter math problem: \n")
print(problem + " = " + str(solve(problem)))
