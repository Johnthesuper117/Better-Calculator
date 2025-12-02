from calculator import calculate as c
import know as k
import os
import sys
import json

if not os.path.exists("commandSyntax.json"):
  print("Error: commandSyntax.json file not found.")
  sys.exit(1)

jsonFile = open("commandSyntax.json", "r")
commands = json.load(jsonFile)
keyDict = {
    "CALCULATE": commands["CALCULATE"]["shortcut"],
    "LEARN": commands["LEARN"]["shortcut"],
    "END": commands["END"]["shortcut"]
}

usercommand = ""
problem = ""

def command(command, parameter):
  if keyDict["CALCULATE"] == "-c":
    print(f"{parameter} = {c(parameter)}")


def commandLine():
  usercommand = input(f"C:/>")
  command(command=usercommand.split(' ', 1)[0], parameter=f"{usercommand.split(' ', 1)[1]}")


while True:
  commandLine()

"""
if usercommand == keyDict["CALCULATE"]:
  #print("Make sure to use ' ' to separate operators, brackets, and numbers. Use * for multiplication, / for division, ^ for powers, sqrt for square root and pi for Pi")    
  #problem = input("Enter math problem: \n")

  print(f"{problem} = {c.calculate(problem)}")
elif usercommand == keyDict["LEARN"]:
  print("What would you like to learn?")
  action = input(f"Here is a list of actions:\n\n - Perfect Square (1)\n\n - Fibonacci Sequence (2)\n\n")
  print(f"\n{k.knowledge(action)}")
elif usercommand == keyDict["END"]:
  print("Ending project")
  sys.exit(0)
else:
  print(f"{usercommand.index('-')+1}")
  print("Action does not exist")

"""