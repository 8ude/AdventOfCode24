forward_string = "XMAS"
backward_string = "SAMX"

def text_file_to_2d_array(filename):
    with open(filename, 'r') as f:
        array_2d = [list(line.strip()) for line in f.readlines()]
    return array_2d

puzzle_array = text_file_to_2d_array("Day4Input.txt")

def check_for_xmas(array_2d):
    xmas_count = 0
    # Define positions
    movements = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not i == j == 0]

    # Copy the original array into new one for storing changes
    new_array_2d = [row[:] for row in array_2d]

    for y in range(len(array_2d)):  # row
        for x in range(len(array_2d[y])):  # column
            if array_2d[y][x] != "X": #WE'RE LOOKING FOR XMAS! LOOK FOR THE X'S!
                continue
            for move in enumerate(movements):
                test_mas = "X"
                for i in range(1,4):
                    new_x = x+i * move[1][0]
                    new_y = y+i * move[1][1]
                    if new_x<0 or new_y<0 or new_x>=len(array_2d) or new_y>=len(array_2d[y]):
                        break
                    test_mas += array_2d[new_y][new_x]
                    if test_mas == "XMAS":
                        xmas_count+=1
    return xmas_count
xmases = check_for_xmas(puzzle_array)
print("part 1 xmas count " + str(xmases))

#part 2:
def check_for_crossmas(array_2d):
    crossmas_count = 0
    for y in range(len(array_2d)):  # row
        for x in range(len(array_2d[y])):  # column
            if array_2d[y][x] != "A": #Look for the A's
                continue
            
            test_mas = ""
            first_mas = False
            for i in range(-1,2):
                #check top right to bottom left diagonal for MAS or SAM
                new_x = x+i
                new_y = y+i
                if new_x<0 or new_y<0 or new_x>=len(array_2d) or new_y>=len(array_2d[y]):
                    break
                test_mas += array_2d[new_y][new_x]
            if test_mas == "MAS" or test_mas == "SAM":
                test_second_mas = ""
                for j in range(1, -2, -1):
                    new_x = x-j
                    new_y = y+j
                    if new_x<0 or new_y<0 or new_x>=len(array_2d) or new_y>=len(array_2d[y]):
                        break
                    test_second_mas += array_2d[new_y][new_x]
                if test_second_mas == "MAS" or test_second_mas == "SAM": 
                     crossmas_count += 1  
    return crossmas_count
xmases = check_for_crossmas(puzzle_array)
print("part 2 xmas count " + str(xmases))