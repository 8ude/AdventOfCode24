
with open("Day25Input.txt") as input_file:
    #break up the data into chunks demarcated by blank lines
    input_data = input_file.read().strip().split('\n\n')
    
locks = []
keys = []

for data_block in input_data:
    rows = data_block.splitlines()
    #we're really only interested in the number of pins, for both locks and keys
    lock_or_key = [list(row) for row in rows]
    #init our count as an array of zeros, the length of the first row
    count = [0]*len(lock_or_key[0])
    for pins in lock_or_key:
        for i, char in enumerate(pins):
            if char == '#':
                count[i] += 1
    #clear whether it's a lock or key from the first entry of the first row
    if lock_or_key[0][0] == '#':
        #count up number of pins in each col, make this into an array
        locks.append(count)
    else:
        keys.append(count)

def check_match(lock, key):
    for l, k in zip(lock, key):
        #took me a minute to figure this out because the prompt is confusingly written;
        #first pin height is not counted for some reason; locks and keys all have actual pin count 1-6,
        #and match with a combined height of 7 or less
        if l + k <= 7:
            continue
        else:
            return False
    return True

num_pairs = 0

for lock in locks:
    for key in keys:
        if check_match(lock, key):
            num_pairs += 1

print(f"total pairs: {num_pairs}")
