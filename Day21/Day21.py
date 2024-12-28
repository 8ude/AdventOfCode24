#solution from salt-die -- https://github.com/salt-die/Advent-of-Code/blob/main/2024/day_21.py
#annotating for ~~learning~~

#see https://docs.python.org/3/library/functools.html
from functools import cache
#see https://docs.python.org/3/library/itertools.html#itertools.starmap
#starmap is akin to map(func, it) - which applies "func" to "it"
#starmap works if it are tuples - in our usecase our function has two arguments and we want to pass these as a tuple
from itertools import starmap

#sliding_window does kind of what it sounds like - has a window that slides along an iterable
#it uses islice and tee from itertools
from aoc_lube.utils import sliding_window

with open("Day21Input.txt") as data_input:
    data_string = data_input.read()
CODES = data_string.splitlines()

#make a dictionary associating each numpad value (as a string) with coordinates (0-4, 0-2)
NUMPAD = {
    key: (y, x)
    for y, row in enumerate(["789", "456", "123", "_0A", "<v>"])
    for x, key in enumerate(row)
}
_Y, _X = NUMPAD["_"]


@cache
#not exactly sure why to use cache here?
def paths(a, b):
    (uy, ux), (vy, vx) = NUMPAD[a], NUMPAD[b]
    dy, dx = vy - uy, vx - ux
    path = f"{'v' * dy}{'0' * -dy}{'>' * dx}{'<' * -dx}"
    paths = []
    if ux != _X or vy != _Y:
        paths.append(f"{path}A")
    if dy and dx and (uy != _Y or vx != _X):
        paths.append(f"{path[::-1]}A")
    return paths

@cache

def nkeys(code, nrobots=2):
    #need to figure out what sliding window does
    all_paths = starmap(paths, sliding_window("A" + code))
    if nrobots == 0:
        return sum(len(path[0]) for path in all_paths)
    return sum(min(nkeys(path, nrobots - 1) for path in paths) for paths in all_paths)

def part_one():
    return sum(nkeys(code) *int(code[:-1]) for code in CODES)

def part_two():
    return sum(nkeys(code, nrobots=25) * int(code[:-1]) for code in CODES)

print(f"salt-die soln p1: {part_one()}")
print(f"salt-die soln p2: {part_two()}")