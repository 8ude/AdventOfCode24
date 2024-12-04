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


#Part 2 

#setting up global variable
bool_val = True

#processing per string
def find_patterns(s):
    global bool_val

    #dictionary of regex patterns we're looking for
    patterns = {
        "do()": re.compile(r'do\(\)'),
        "don't()": re.compile(r'don\'t\(\)'),
        "mul": re.compile(r'mul\((\d+),(\d+)\)') #note that this returns a match group with the integers but not the comma, for convenience
    }

    matches = []
    #go through each dictionary of paterns
    for key, pattern in patterns.items():
        #go through string until we find matches for that pattern in our dictionary
        for match in pattern.finditer(s):
            if key == "mul":
                #matches in python have some return data, including start(), end(), span() - a tuple with start and end, and group() which is the string returned by the regex 
                matches.append((key, match.start(), match.group(1), match.group(2)))
            else:
                #we don't care about the group() of the regex for "do" and "don't" since it matches the key
                matches.append((key, match.start()))

    matches.sort(key=lambda x: x[1])  # Sort by position - we've defined this as the second entry in the match object

    line_sum = 0 #running sum for the line
    #iterate through the sorted matches
    for match in matches:
        if match[0] == "do()":
            bool_val = True
            print(f'Pattern "{match[0]}" found at position {match[1]} : bool_val is now {bool_val}')
        elif match[0] == "don't()":
            bool_val = False
            print(f'Pattern "{match[0]}" found at position {match[1]} : bool_val is now {bool_val}')
        elif match[0] == "mul" and bool_val == True:
            x, y = int(match[2]), int(match[3])
            result = x * y  # Perform multiplication
            print(f'Pattern "mul({x},{y})" found at position {match[1]} : result is {result}')
            line_sum += result
    return line_sum

sum = 0

with open ("Day3Input.txt") as dataInput:
    bool_val = True
    for line in dataInput:
        sum += find_patterns(line)
    print("part 2 sum: "+str(sum))