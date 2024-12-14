#solution from github user hortonhearsadan -- https://github.com/hortonhearsadan/aoc-2024/blob/main/aoc_2024/day12.py

with open("Day12Input.txt") as input_data:
    input_string = input_data.read()

from collections import defaultdict

import networkx as nx
from networkx import Graph

DIRECTIONS = (1, -1, 1j, -1j)

def adjacent (node1, node2):
    result_0 = abs(node1[0] - node2[0])
    result_1 = abs(node1[1] - node2[1])
    return abs(node1[0] - node2[0]) == 1 and abs(node1[1] - node2[1]) == 1
 
def part1_2(data):
    #garden is going to be a dictionary with the key as the letter that defines the plot (a group of E's for example). The value of the dictionary is a set containing the coordinates of all these E's
    garden = defaultdict(set)
    for i, row in enumerate(data):
        for j, plot in enumerate(row):
            garden[plot].add(complex(j, -i))

    total_cost = 0
    discout_cost = 0
    outs = defaultdict(list)
    for _plots, locations in garden.items():
        graphs = Graph()
        for location in locations:
            graphs.add_node(location)
            for direction in DIRECTIONS:
                neighbor = location+direction
                if neighbor in locations:
                    graphs.add_edge(location, neighbor)
                else:
                    outs[location].append(neighbor)
        
        subsets = nx.connected_components(graphs)

        for sub in subsets:
            perim_sub = [(n,o) for n in sub for o in outs[n]]
            area = len(sub)
            perim = len(perim_sub)
            sides = perim
            for i, node in enumerate(perim_sub):
                for node2 in perim_sub[i+1 :]:
                    if node == node2:
                        continue
                    if adjacent(node, node2):
                        sides -=1
            disc_cost = area * sides
            full_cost = area * perim
            total_cost += full_cost
            discout_cost += disc_cost
    return total_cost, discout_cost
data_by_line = input_string.splitlines()
part1_result, part2_result = part1_2(data_by_line)

print(f"part 1: {part1_result}")
print(f"part 2: {part2_result}")