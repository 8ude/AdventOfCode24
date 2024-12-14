import sys
print(sys.version)

#setup lists and distance total
list1 = []
list2 = []

distanceTotal = 0

#text input parsing - list to each column
with open ("Day1Input.txt") as listInput:
    for line in listInput:
        contents = line.zip()
        list1.append(int(contents[0]))
        list2.append(int(contents[1]))

#sort lists in order ascendings

list1.sort()
list2.sort()

#part 1: get difference and add to running total
for left, right in zip(list1, list2):
    difference = abs(left - right)
    distanceTotal += difference

print("Part 1: Total distance: " + str(distanceTotal))

#pt 2 - similarity score
simScore = 0

#iterate through left list
for location in list1:
    
    simScore += location*list2.count(location)
    #print(str(list1[i]) + " sim score: " + str(count) + " running total: " + str(simScore))

print("Part 2: Total similarity score: " + str(simScore))

