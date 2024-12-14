#stolen solution from salt-die -- https://github.com/salt-die/Advent-of-Code/blob/main/2024/day_08.py
#using for learning (and hopefully using their tool to make a visualizer later???)

#combinations returns combinations of the iteratable (like a list)
#example: combinations('ABCD', 2) -> AB AC AD BC BD CD
from itertools import combinations

import numpy as np

#could be cleaner; author has special git tools for ingesting puzzle inputs
data_string = ""
with open("Day8Test.txt") as input_data:
    data_string = input_data.read()
#this makes a numpy array
#note that list(string) makes a list with each character in the string as an element
#so this will split each new line in the mega-line from the input file, create a character-by-character list from that line, and make a numpy array with all of those lists.
GRID = np.array([list(line) for line in data_string.splitlines()])
H,W = GRID.shape

#https://numpy.org/doc/stable/reference/generated/numpy.unique.html
#unique(ar) returns the sorted unique elements of an array
#in this case, freq will be each string character (as a np.str_ type)
FREQUENCIES = [freq for freq in np.unique(GRID) if freq != "."]

#numpy (and most languages I guess) is row-major --> y coordinate is first
def inbounds(y,x):
    return 0 <=y < H and 0 <= x < W

def mark_podes(y, x, dy, dx, podes, part):
    if part == 1:
        if inbounds(y+dy, x+dx):
            #part 1 is a check for just one anti pode
            podes[y+dy, x+dx] = 1
        return
    while inbounds(y,x):
        #part 2 checks for all possible antipodes within the bounds
        podes[y,x] = 1
        y += dy
        x += dx

def sum_antipodes(part):
    #init antipodes with zeros
    antipodes = np.zeros((H,W), int)
    for freq in FREQUENCIES:
        #ok. argwhere is finding where in the array (GRID) we have our frequency (freq) and returns an array of these locations -- [loc1 = (y1, x1), loc2 = (y2, x2).......]
        #combinations is then making an array of all the combinations of 2 locations - [(loc1, loc2),(loc1, loc3).......]
        #then a and b are the first and second location of each pair, respectively
        for a, b in combinations(np.argwhere(GRID == freq), r=2):
            #this is some "unpack" trickery
            #mark_podes takes 4 arguments for coordinates: x, y, dx, dy
            #unpack assigns y and x to the corresponding elements of a (which is a location in the form [y,x])
            #then dy and dx are assigned as ay - by and ax - bx
            #written out, the arguments are (ay, ax, ay-by, ax-bx, antipodes, part)

            #in summary, we're going through the list of pairs of matching characters, and marking_podes based on the locations of the pairs (a and b) and the distance between them (a-b and b-a)
            mark_podes(*a, *a - b, antipodes, part)
            mark_podes(*b, *b - a, antipodes, part)
    #clever use of sum() so we don't need to check for uniqueness (because we initialized with zeroes)
    return antipodes.sum()

print(f"Part 1: {sum_antipodes(1)}")
print(f"Part 2: {sum_antipodes(2)}")