import calculate as c
import knowledge as mK
import os
import sys
import json

usercommand = ""

jsonFile = open("commands.json", "r")
commands = json.load(jsonFile)

"""
while usercommand.upper() != "END":
  action = input(f"Choose an action:\n\n - Calculate (1)\n\n - Learn (2)\n\n - END (0)\n\n")
  if action.upper() == "CALCULATE" or action.upper() == "1":
   print("Make sure to use ' ' to separate operators, brackets, and numbers. Use * for multiplication, / for division, ^ for powers, sqrt for square root and pi for Pi")    
   problem = input("Enter math problem: \n")
   print(f"{problem} = {eval(problem)}")
  elif action.upper() == "LEARN" or action.upper() == "2":
    print("What would you like to learn?")
    action = input(f"Here is a list of actions:\n\n - Perfect Square (1)\n\n - Fibonacci Sequence (2)\n\n")
    print(f"\n{mK.knowledge(action)}")
  elif action.upper() == "END" or action.upper() == "0":
    print("Ending project")
    break
  else:
    print("Action does not exist")
    """
