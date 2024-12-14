#this first part is from user salt-die, but part two doesn't work
#https://github.com/salt-die/Advent-of-Code/blob/main/2024/day_10.py

from utils import grid_steps, ilen

import networkx as nx

def parse_raw(filename):
    with open(filename) as file_input:
        grid = file_input.read().splitlines()
    trailheads = []
    summits = []
    G = nx.DiGraph()
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "0":
                trailheads.append((y,x))
            elif char == "9":
                summits.append((y,x))
            G.add_node((y,x), value=int(char))
    nodes = G.nodes(data="value")
    for a, b in grid_steps(4, len(grid), len(grid[0])):
        if nodes[b] - nodes[a] == 1:
            G.add_edge(a,b)
    return G, trailheads, summits

G, TRAILHEADS, SUMMITS = parse_raw("Day10Input.txt")

def part_one():
    return sum(nx.has_path(G,a,b) for a in TRAILHEADS for b in SUMMITS)

def part_two():
    #something is wrong with this - returns the same answer as part 1
    #code from github didn't compile because of a sum function around ilen()
    #looking at utils - ilen returns an integer sum
    return ilen(
            nx.all_simple_edge_paths(G,a,b)
            for a in TRAILHEADS
            for b in SUMMITS
            if nx.has_path(G,a,b)
        )
    

print(f"part 1: {part_one()}")
print(f"part 2: {part_two()}")

#alternate - from user blbrault

map: [[int]] = []

with open('Day10Input.txt', 'r') as file:
    for line in file:
        map_row = []
        for char in line.strip():
            map_row.append(int(char))
        map.append(map_row)

def solve_part1():
    def walk_trail(x: int, y: int, end_positions: set[tuple[int, int]]) -> int:
        height = map[y][x]
        if height == 9:
            end_positions.add((x, y))
            return

        # left
        if x > 0 and map[y][x - 1] == height + 1:
            walk_trail(x - 1, y, end_positions)
        # up
        if y > 0 and map[y - 1][x] == height + 1:
            walk_trail(x, y - 1, end_positions)
        # right
        if x < len(map[y]) - 1 and map[y][x + 1] == height + 1:
            walk_trail(x + 1, y, end_positions)
        # down
        if y < len(map) - 1 and map[y + 1][x] == height + 1:
            walk_trail(x, y + 1, end_positions)

    total_score = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                end_positions = set()
                walk_trail(x, y, end_positions)
                total_score += len(end_positions)

    print('Sum of scores for all trailheads (part 1):', total_score)

def solve_part2():
    def walk_trail(x, y) -> int:
        height = map[y][x]
        if height == 9:
            return 1

        score = 0
        # left
        if x > 0 and map[y][x - 1] == height + 1:
            score += walk_trail(x - 1, y)
        # up
        if y > 0 and map[y - 1][x] == height + 1:
            score += walk_trail(x, y - 1)
        # right
        if x < len(map[y]) - 1 and map[y][x + 1] == height + 1:
            score += walk_trail(x + 1, y)
        # down
        if y < len(map) - 1 and map[y + 1][x] == height + 1:
            score += walk_trail(x, y + 1)
        return score

    total_score = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                total_score += walk_trail(x, y)

    print('Sum of ratings for all trailheads (part 2):', total_score)

solve_part1()
solve_part2()