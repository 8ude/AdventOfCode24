#build map
def text_file_to_2d_array(filename):
    with open(filename, 'r') as f:
        array_2d = [list(line.strip()) for line in f.readlines()]
    return array_2d

field = text_file_to_2d_array("Day6Input.txt")

#part 1

#make direction list, in order of rotation
directions = [(0,-1), (1,0), (0,1), (-1,0)]

#visited positions as a dictionary so we don't double count
p1_visited = {}

#debug visualizer for test
def printField(pos: tuple):
    for y in range(len(field)):
        line = ""
        for x in range(len(field[y])):
            if(x == pos[0] and y == pos[1]):
                line += "X"
            else:
                line += field[y][x]
        print(line)
    print()

#init vars
dir = 0
x = -1
y = -1

#find initial position
for i, row in enumerate(field):
    for j, c in enumerate(row):
        if c == "^":
            x = j
            y = i
            p1_visited[x,y] = True

while(True):
    #debug print for test
    if(len(field) < 20):
        printField((x, y))
    nextX = x + directions[dir][0]
    nextY = y + directions[dir][1]
    if(nextX < 0 or nextX>= len(field[0]) or nextY < 0 or nextY >=len(field)):
        break
    if(field[nextY][nextX] == "#"):
        dir += 1
        if(dir == 4): dir = 0
        continue
    x = nextX
    y = nextY
    p1_visited[x,y] = True

#part 2

print(f"part 1: {len(p1_visited)}" )

