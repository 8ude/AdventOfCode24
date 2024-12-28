from heapq import heappop, heappush

from aoc_lube.utils import extract_maze

with open("Day16Input.txt") as input_file:
    input_string = input_file.read()

#bit of abstracted magic happening with extract_maze
#I believe every position is paired with a graph of it's abstracted neighbors
MAZE = extract_maze(input_string)[1]
START, END = (139, 1), (1, 139)


def find_min_path():
    min_scores = {}
    best_seats = set()
    best_score = -1
    heap = [(0, START, (0, 1), [])]
    while heap:
        score, pos, dir, seats = heappop(heap)
        if pos == END:
            best_score = score
            best_seats.update(seats)
            continue

        for neighbor in MAZE[pos]:
            new_dir = neighbor[0] - pos[0], neighbor[1] - pos[1]
            #clever use of ** which is an exponential operator
            #(new_dir != dir) ==> (1) if turning; (0) if not
            #1001 ^ 0 = 1 so add one if going the same direction
            #1001 ^ 1 = 1001 so add 1001 if going a new direction
            new_score = score + 1001 ** (new_dir != dir)
            if min_scores.setdefault((neighbor, new_dir), new_score) >= new_score:
                min_scores[neighbor, new_dir] = new_score
                heappush(heap, (new_score, neighbor, new_dir, seats + [pos]))

    return best_score, len(best_seats) + 1


def part_one():
    return find_min_path()[0]


def part_two():
    return find_min_path()[1]

sd_p1 = part_one()
sd_p2 = part_two()
print(f"salt-die soln part 1: {sd_p1}")
print(f"salt-die soln part 2: {sd_p2}")