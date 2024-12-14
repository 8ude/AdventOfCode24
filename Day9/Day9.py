#solution from user salt-die -- https://github.com/salt-die/Advent-of-Code/blob/main/2024/day_09.py

filename = "Day9Input.txt"

with open(filename) as data_input:
    data_line = data_input.read()

DISK = list(map(int, data_line))

def get_memory():
    used, free = [],[]
    pos = 0
    for i, size in enumerate(DISK):
        #python evaluates i%2 as true if it is non zero (i.e. i is an odd number)
        #in the problem description, "free" spaces are marked by the odd numbers
        #i // 2 would give the floor division. this is a way of getting the file ID for the block, because the free spaces (odd indices) have no file id. Not sure if the floor component is needed..
        (free if i % 2 else used).append([pos, size, i // 2])
        pos += size
    return used, free

def triangular_sum(pos, size):
    return pos * size + (size * (size-1) // 2)

def checksum(used):
    return sum(file_id * triangular_sum(pos,size) for pos, size, file_id in used)

def move(free_info, file_info):
    file_info[0] = free_info[0]
    free_info[0] += file_info[1]
    free_info[1] -= file_info[1]

def part_one():
    used, free = get_memory()
    files = reversed(used)
    file_info = next(files)
    fragged = []
    for free_info in free:
        if free_info[0] > file_info[0]:
            break
        while free_info[1] >= file_info[1]:
            move(free_info, file_info)
            file_info = next(files)
        if free_info[1] > 0:
            free_info[2] = file_info[2]
            fragged.append(free_info[:])
            file_info[1] -= free_info[1]
            free_info[1] = 0
    return checksum(used) + checksum(fragged)

def part_two():
    used, free = get_memory()
    for file_info in reversed(used):
        for free_info in free:
            if free_info[0] > file_info[0]:
                break
            if free_info[1] >= file_info[1]:
                move(free_info, file_info)
                break
    return checksum(used)

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")