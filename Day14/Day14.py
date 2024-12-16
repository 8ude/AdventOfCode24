#corey's solution (part 1)

width = 101
height = 103

robot_status = []

def parse_input(text_file):
    with open(text_file) as file_input:
        for line in file_input.read().splitlines():
            #first tuple is the position, second is the velocity - split at the space by default
            string_elements = line.split()
            #reading left to right -- we're making an array of tuples that are cast to ints using map
            #since these are given the form p=a1,a2 v=b1,b2, we can ignore the part before the '=' signs (0 index).
            #we split that second element (1 index) at the comma to form the tuple. Do this for both of the string_elements
            status = [tuple(map(int, el.split("=")[1].split(","))) for el in string_elements]
            robot_status.append(status)

def part_one(timeCount):

    new_robot_status = robot_status
    quad_counts = [0]*4
    for i, robot in enumerate(new_robot_status):
        orig_robot = robot
        #this isn't working for some fucking reason
        newX = (robot[0][0] + (timeCount*robot[1][0]))%width
        newY = (robot[0][1] + (timeCount*robot[1][1]))%height
        robot[0] = (newX, newY)
        new_robot_status[i] = robot
        middle_width = width // 2
        if (newX < (width // 2) and newY < (height // 2)):
            quad_counts[0] += 1
        elif (newX > (width // 2) and newY < (height // 2)):
            quad_counts[1] += 1
        elif (newX > (width // 2 ) and newY > (height // 2)):
            quad_counts[2] += 1
        elif (newX < (width // 2 ) and newY > (height // 2)):
            quad_counts[3] += 1
    return quad_counts[0]*quad_counts[1]*quad_counts[2]*quad_counts[3]
#testing
#parse_input("Day14Test.txt")
#p1_test = part_one(100)
#print(f"part one test safety: {p1_test}")


#something weird happened with defining/redefining length/width

#couldn't figure out part 2, so I'm inspecting others solutions for ~*learning*~

#input
parse_input("Day14Input.txt")
p1_real = part_one(100)
print(f"part one full safety: {p1_real}")
 
##############################################
###solution from topaz?? or u/the_cassiopeia??
#I admit I don't fully understand this one
###############################################
import re
from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class Robot:
    col: int
    row: int
    vcol: int
    vrow: int


def load_robots(filename):
    #using regex to find integers
    pattern = re.compile(r"-?\d+")
    with open(filename, "rt") as fin:
        nums = [int(m.group()) for m in re.finditer(pattern, fin.read())]
    return [Robot(*nums[i : i + 4]) for i in range(0, len(nums), 4)]


def move(robos, seconds, area_rows, area_cols):
    for r in robos:
        r.row = (r.row + r.vrow * seconds) % area_rows
        r.col = (r.col + r.vcol * seconds) % area_cols


def find_tree_second(robos, current_seconds, area_rows, area_cols):
    row_var_thres = np.var([r.row for r in robos]) * 0.5
    col_var_thres = np.var([r.col for r in robos]) * 0.5
    row_low_var, col_low_var = 0, 0

    # look for first second when variance is low (indicates clustered robots)
    while row_low_var == 0 or col_low_var == 0:
        current_seconds += 1
        move(robos, 1, area_rows, area_cols)
        if row_low_var == 0 and np.var([r.row for r in robos]) < row_var_thres:
            row_low_var = current_seconds % area_rows
        if col_low_var == 0 and np.var([r.col for r in robos]) < col_var_thres:
            col_low_var = current_seconds % area_cols

    # low row variance occurs every area_rows seconds
    # low col variance occurs every area_cols seconds
    # find second when both are low together, i.e. find x and y in this equation:
    # row_low_var + area_rows*x = col_low_var + area_cols*y

    # brute force solution
    x, y = 1, 1
    while True:
        left_side = row_low_var + area_rows * x
        right_side = col_low_var + area_cols * y
        if left_side == right_side:
            return left_side
        if left_side < right_side:
            x += 1
        else:
            y += 1


def safety_factor(robos, area_rows, area_cols):
    mid_row, mid_col = area_rows // 2, area_cols // 2
    quadrants = {(True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0}

    for r in robos:
        if r.row == mid_row or r.col == mid_col:
            continue
        quadrants[r.row < mid_row, r.col < mid_col] += 1

    return (
        quadrants[True, True]
        * quadrants[True, False]
        * quadrants[False, True]
        * quadrants[False, False]
    )


def main():
    robos = load_robots("Day14Input.txt")
    area_rows, area_cols = 103, 101

    move(robos, 100, area_rows, area_cols)
    print(f"Part 1: {safety_factor(robos, area_rows, area_cols)}")
    print(f"Part 2: {find_tree_second(robos, 100, area_rows, area_cols)}")


if __name__ == "__main__":
    main()

#########################################################
#####################################################################
#another solution - really short one from salt-die (albiet with it's own library..)
#https://github.com/salt-die/Advent-of-Code/blob/main/2024/day_14.py
#####################################################################
############################################################

from itertools import count

import numpy as np
from utils import extract_ints

data_string = ''
with open("Day14Input.txt") as file_input:
    data_string = file_input.read()
#numpy has some convenient features it seems
#it's creating an array from the iterator that goes through the data string and uses regex (and map) to find the integers. Reshape is making that into an array of (I'm assuming -1 means) indefinite 'rows' of 2 entries each
DATA = np.fromiter(extract_ints(data_string), int).reshape(-1, 2)
POS = DATA[::2]
VEL = DATA[1::2]
DIM = np.array([101, 103])


def sd_part_one():
    pos = (POS + 100 * VEL) % DIM
    not_centered = pos[np.all(pos != DIM // 2, axis=-1)]
    return np.bincount((not_centered < DIM // 2) @ (2, 1)).prod()


def sd_part_two():
    for i in count():
        if np.unique((POS + i * VEL) % DIM, axis=0).shape == POS.shape:
            return i

sd_p1 = sd_part_one()
sd_p2 = sd_part_two()
print(f"salt-die solution p1: {sd_p1}")
print(f"salt-die solution p2: {sd_p2}")
