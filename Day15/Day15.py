#learning solutions: github user TheBlackOne
#https://github.com/TheBlackOne/Advent-of-Code/blob/master/2024/Day15_1.py

input = ""
with open("Day15Input.txt") as f:
    input = f.read()

directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

#added "p1" bool as an argument because the character of interest changes for part 2
def get_all_box_coords(grid, p1):
    box_coords = set()
    
    for y, line in enumerate(grid):
        if p1:
            for x in [x for x, field in enumerate(line) if field == "O"]:
                box_coords.add((x, y))
        else:
            for x in [x for x, field in enumerate(line) if field == "["]:
                box_coords.add((x, y))


    return box_coords

def print_grid(grid):
    global screen
    for line in grid:
        line = "".join(line)
        print(line)


def get_grid_field(pos):
    x, y = pos
    return grid[y][x]

def swap_grid_fields(pos1, pos2):
    """modifies the global grid to swap pos1 and pos2
    Params:
    pos1: the first position, in (x, y) integer format
    pos2: the second position"""
    global grid

    x1, y1 = pos1
    x2, y2 = pos2

    grid[y1][x1], grid[y2][x2] = grid[y2][x2], grid[y1][x1]

#for part 1
def collect_box_candidates(pos, direction):
    global grid

    candidates = []
    while True:
        pos = tuple(map(sum, zip(pos, direction)))
        x, y = pos
        field = grid[y][x]
        if field == "O":
            candidates.append(pos)
        elif field == "#":
            candidates = []
            break
        elif field == ".":
            candidates.append(pos)
            break

    return candidates

#for part 2
def collect_box_candidates_vertical(pos, direction):
    global grid

    positions = [pos]

    candidates = []

    keep_searching = True
    while keep_searching:
        new_candidates = set()
        add_new_candidates = True
        for position in positions:
            neighbour_pos = tuple(map(sum, zip(position, direction)))
            neighbour_field = get_grid_field(neighbour_pos)

            if neighbour_field == "[":
                new_candidates.add(neighbour_pos)
                x, y = neighbour_pos
                new_candidates.add((x + 1, y))
            elif neighbour_field == "]":
                new_candidates.add(neighbour_pos)
                x, y = neighbour_pos
                new_candidates.add((x - 1, y))
            elif neighbour_field == "#":
                candidates = []
                keep_searching = False
                add_new_candidates = False
                break
        if len(new_candidates) == 0:
            keep_searching = False

        positions = new_candidates
        if add_new_candidates:
            candidates.append(new_candidates)

    return candidates

#for part 2
def collect_box_candidates_horizontal(pos, direction):
    global grid

    candidates = []
    while True:
        pos = tuple(map(sum, zip(pos, direction)))
        field = get_grid_field(pos)
        if field == "[" or field == "]":
            candidates.append(pos)
        elif field == "#":
            candidates = []
            break
        elif field == ".":
            break

    return candidates

def part_1():
    global grid 
    grid = []

    robot_pos = None
    layout, movements = input.split("\n\n")
    for y, line in enumerate(layout.splitlines()):
        possible_x = line.find("@")
        if possible_x > -1:
            robot_pos = (possible_x, y)
            # line = line.replace("@", ".")
        grid.append(list(line))

    movements = list(movements.replace("\n", ""))

    #going through movements list
    for movement in movements:
        direction = directions[movement]
        new_robot_pos = tuple(map(sum, zip(robot_pos, direction)))

        neighbour = get_grid_field(new_robot_pos)

        if neighbour == "O":
            box_candidates = collect_box_candidates(robot_pos, direction)
            if len(box_candidates) > 0:
                box_pos1 = box_candidates[0]
                box_pos2 = box_candidates[-1]

                swap_grid_fields(box_pos1, box_pos2)

                neighbour = get_grid_field(box_pos1)
        if neighbour == ".":
            swap_grid_fields(robot_pos, new_robot_pos)
            robot_pos = new_robot_pos

    box_coords = get_all_box_coords(grid, True)
    #didn't know about this - you can use for to iterate with both items in a tuple -- box_coords is a set of (x,y) coords
    sum_coords = sum(x + y * 100 for x, y in box_coords)
    print(f"Carsten's solution part 1: {sum_coords}")

def part_2():
    global grid
    grid = []

    robot_pos = None
    layout, movements = input.split("\n\n")
    for y, line in enumerate(layout.splitlines()):
        new_line = ""
        for x, field in enumerate(line):
            if field == "@":
                new_line += "@."
                robot_pos = (x * 2, y)
            elif field == "#" or field == ".":
                new_line += field * 2
            elif field == "O":
                new_line += "[]"

        grid.append(list(new_line))

    # print_grid(grid)

    movements = list(movements.replace("\n", ""))

    step = 0
    for movement in movements:
        direction = directions[movement]
        new_robot_pos = tuple(map(sum, zip(robot_pos, direction)))

        neighbour = get_grid_field(new_robot_pos)

        if movement == "<" or movement == ">":
            if neighbour == "[" or neighbour == "]":
                box_candidates = collect_box_candidates_horizontal(robot_pos, direction)
                if len(box_candidates) > 0:
                    for box_pos in box_candidates[::-1]:
                        new_box_pos = tuple(map(sum, zip(box_pos, direction)))
                        swap_grid_fields(box_pos, new_box_pos)
                    neighbour = get_grid_field(new_robot_pos)
        else:
            if neighbour == "[" or neighbour == "]":
                box_candidates = collect_box_candidates_vertical(robot_pos, direction)
                for boxes in box_candidates[::-1]:
                    for box_pos in boxes:
                        new_box_pos = tuple(map(sum, zip(box_pos, direction)))
                        swap_grid_fields(box_pos, new_box_pos)
                neighbour = get_grid_field(new_robot_pos)

        if neighbour == ".":
            swap_grid_fields(robot_pos, new_robot_pos)
            robot_pos = new_robot_pos

        step += 1

    # print_grid(grid)
    box_coords = get_all_box_coords(grid, False)
    sum_coords = sum(x + y * 100 for x, y in box_coords)
    print(f"Carsten's solution part 2: {sum_coords}")

if __name__ == "__main__":
    part_1()
    part_2()


