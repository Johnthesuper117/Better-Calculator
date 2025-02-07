import math

def knowledge(what):
    perfectSquares = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100, 11:121, 12:144}
    
    if what.upper() == 'PERFECT SQUARE':
        return perfectSquares
    elif 


print("What would you like to learn?")
action = input(f"Here is a list of actions:\n\n - Perfect Square\n\n - Fibonacci Sequence")
print(f"\n{knowledge(action)}")
