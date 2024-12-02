#in case of visualizer...
from p5 import *

def sign(num):
    return (num > 0) - (num < 0)

safeCount = 0
with open ("Day2Input.txt") as dataInput:
    for line in dataInput:
        #parse line into an "report" array
        report = list(map(int, line.split()))
        unsafeReport = False

        #ascending/descending given by first delta
        reportDir = sign(report[1]-report[0])

        #early out if they're the same
        if (reportDir == 0):
            print("unsafe")
            unsafeReport = True
        else:
            #iterate through remaining entries
            for i in range(1, len(report)):
                #check if direction matches and difference is "safe"
                dif = report[i]-report[i-1]
                if sign(dif)!=reportDir or abs(dif) > 3:
                    unsafeReport = True;
                    print("unsafe")
                    break
        if unsafeReport == False:
            print("safe")
            safeCount+=1
print("safe count: " + str(safeCount))


