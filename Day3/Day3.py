import re

sum = 0

#Part 1
with open ("Day3Input.txt") as dataInput:
    for line in dataInput:

        matches = re.findall(r'mul\((\d+),(\d+)\)', line)

        for match in matches:
            x, y = map(int, match)
            sum += x*y
            print("P1 total:" + str(sum))