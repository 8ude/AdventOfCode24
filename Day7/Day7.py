#Code by JamesPeralta

def file_to_lines(input_file):
    data_array = []
    with open(input_file, 'r') as data_input:
        for line in data_input:
            data_array.append(line)
    return data_array


#recursive function:
#returns true if we can get to the target by using some combination of added and multiplied (or concat - part 2) between elements
#otherwise returns false
def back_track(curr_sum, target, index, elements):
    if index == len(elements):
        return curr_sum == target
    
    candidate = elements[index]
    added = back_track(curr_sum + candidate, target, index + 1, elements)
    multiplied = back_track(curr_sum * candidate, target, index + 1, elements)
    concat = back_track(int(f"{curr_sum}{candidate}"), target, index+1, elements)
    #if added or multiplied gives us the correct 
    return added or multiplied or concat

#part 1
total = 0
input_data = file_to_lines("Day7Input.txt")
for line in input_data:
    #parse data based on format
    expected, elements = line.split(": ")
    terms = list(map(lambda x: int(x), elements.split(" ")))
    #starting at index argument = 1 because we initialize the current sum as the 0-index element
    if(back_track(terms[0], int(expected), 1, terms)):
        total += int(expected)

print ("part 2: " + str(total))
