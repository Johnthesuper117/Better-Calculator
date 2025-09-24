import calculate as c
import knowledge as k
import os
import sys
import json

if not os.path.exists("commandSyntax.json"):
  print("Error: commandSyntax.json file not found.")
  sys.exit(1)

jsonFile = open("commandSyntax.json", "r")
commands = json.load(jsonFile)

usercommand = ""
problem = ""

def commandLine():
  usercommand = input(f"C:/>")

  if usercommand.index("-")+1 == commands["CALCULATE"]["shortcut"]:
    #print("Make sure to use ' ' to separate operators, brackets, and numbers. Use * for multiplication, / for division, ^ for powers, sqrt for square root and pi for Pi")    
    #problem = input("Enter math problem: \n")

    print(f"{problem} = {c.calculate(problem)}")
  elif usercommand == commands["LEARN"]["shortcut"]:
    print("What would you like to learn?")
    action = input(f"Here is a list of actions:\n\n - Perfect Square (1)\n\n - Fibonacci Sequence (2)\n\n")
    print(f"\n{k.knowledge(action)}")
  elif usercommand == commands["END"]["shortcut"]:
    print("Ending project")
    sys.exit(0)
  else:
    print("Action does not exist")

while True:
  commandLine()