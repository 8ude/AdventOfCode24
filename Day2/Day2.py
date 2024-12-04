#in case of visualizer...
#from p5 import *

def sign(num):
    return (num > 0) - (num < 0)

#PART 1
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
print("Part 1 safe count: " + str(safeCount))

#this is a bit of a mess - re-check the array after an entry is removed
def recheckReport(report, dir):
    for i in range(1, len(report)):
        #check if direction matches and difference is "safe"
        dif = report[i]-report[i-1]
        if sign(dif)!=dir or abs(dif) > 3:
            return True
    return False
    

#PART 2
safeCount = 0
with open ("Day2Test.txt") as dataInput:
    for line in dataInput:
        #parse line into an "report" array
        report = list(map(int, line.split()))
        unsafeReport = False
        #if still unsafe after removing an entry, then it's an unsafe report
        stillUnsafe = False

        reportDir = sign(report[1]-report[0])
        #special cond if first two are the same
        if (reportDir == 0):
            unsafeReport = True
            #reset direction to second two entries
            reportDir = sign(report[2]-report[1])
            for i in range(2, len(report)):
                #check if direction matches and difference is "safe"
                dif = report[i]-report[i-1]
                if sign(dif)!=reportDir or abs(dif) > 3:
                    stillUnsafe = True;
                    print("still unsafe")
                    break
        #other special conditions - first entry is the problem
        elif (abs(report[1] - report[0])>3):
            unsafeReport = True
            report.pop(0)
            stillUnsafe = recheckReport(report, sign(report[1]-report[0]))
            if (stillUnsafe):
                print("still unsafe")
        else:
            #iterate through remaining entries
            for i in range(1, len(report)):
                #check if direction matches and difference is "safe"
                dif = report[i]-report[i-1]
                if sign(dif)!=reportDir or abs(dif) > 3:
                    unsafeReport = True
                    #try removing this entry
                    report.pop(i)
                    break;
            #if entry is removed, recheck using resized report
            if unsafeReport:
                stillUnsafe = recheckReport(report, reportDir)
                if (stillUnsafe):
                    print("still unsafe")
        if stillUnsafe == False:
            print("safe")
            safeCount+=1
print("Pt 2 safe count: " + str(safeCount))

