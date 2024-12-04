forward_string = "XMAS"
backward_string = "SAMX"

def text_file_to_2d_array(filename):
    with open(filename, 'r') as f:
        array_2d = [list(line.strip()) for line in f.readlines()]
    return array_2d

puzzle_array = text_file_to_2d_array("Day4Test.txt")

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
                    new_x = x+i * move[0]
                    new_y = y+i * move[1]
                    if new_x<0 or new_y<0 or new_x>=len(array_2d) or new_y>=len(array_2d[y]):
                        break
                    test_mas += array_2d[new_y, new_x]
                    if test_mas == "XMAS":
                        xmas_count+=1

            
            #    ni, nj = i + move[0], j + move[1]
            #    if (0 <= ni < len(array_2d) and 0 <= nj < len(array_2d[0])) and \
            #            (0 <= k < len(test_string) and 0 <= len(test_string) - 1 - k < len(test_string)):
                    # Check the neighbour against the corresponding forward and backward neighbour in the string
            #        if not (array_2d[ni][nj] == test_string[k] and array_2d[ni][nj] == test_string[len(test_string) - 1 - k]):
                        # If the check fails, replace that character with '.'
            #            new_array_2d[ni][nj] = '.'

    return xmas_count
xmases = check_for_xmas(puzzle_array)
print("xmas count " + int(xmases))