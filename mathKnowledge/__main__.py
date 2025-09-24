import math

def knowledge(what):
    perfectSquares = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100, 11:121, 12:144}
    
    if what.upper() == 'PERFECT SQUARE' or what.upper() == '1':
        return perfectSquares
    elif what.upper() == 'FIBONACCI SEQUENCE' or what.upper() == '2':
        t = int(input("How many numbers in the Sequence do you whant to see?\n"))
        FibonacciSequence = [0, 1]
        while int(t) > 0:
            FibonacciSequence.append(FibonacciSequence[-1] + FibonacciSequence[-2])
            t -= 1
        print(f"{FibonacciSequence}")
