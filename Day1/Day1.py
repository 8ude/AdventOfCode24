#setup lists and distance total
list1 = []
list2 = []

distanceTotal = 0

#text input parsing - list to each column
with open ("Day1Input.txt") as listInput:
    for line in listInput:
        contents = line.split()
        list1.append(int(contents[0]))
        list2.append(int(contents[1]))

#sort lists in order ascending

list1.sort()
list2.sort()

#part 1: get difference and add to running total
for i, location in enumerate(list1):
    difference = abs(list2[i] - list1[i])
    distanceTotal += difference

print("Part 1: Total distance: " + str(distanceTotal))

#pt 2 - similarity score
simScore = 0

#iterate through left list
for i, location in enumerate(list1):
    count = 0
    for j, location in enumerate(list2):
        if list2[j] == list1[i]:
            count+=1
    #multiply by num times it appears in the right
    #add to running total
    simScore += list1[i]*count
    #print(str(list1[i]) + " sim score: " + str(count) + " running total: " + str(simScore))

print("Part 2: Total similarity score: " + str(simScore))

