#in case of visualizer...
from p5 import *

safeCount = 0
with open ("Day2Test.txt") as dataInput:
    for line in dataInput:
        #parse line into an "report" array
        report = split(dataInput)
        for i in range(1, len(report)):
            if report[i]-report[i-1] > 2:
                print("unsafe")
                break
            else:
                print("safe")
                safeCount+=1
print("safe count: " + (str)safeCount)