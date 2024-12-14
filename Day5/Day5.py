#Part 1

#make rules and stop before the updates section
rules = []
updates = []

def parse_data(datafile):
    switch_to_updates = False
    with open(datafile, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if not stripped_line:  # Switch to second array at first empty line
                switch_to_updates = True
                continue
            if switch_to_updates:
                new_update = [int(i) for i in line.split(',')]
                updates.append(new_update)
            else:
                rule = [int(a) for a in line.split('|')]
                rules.append(rule)

def is_order_valid(instruction, rules):
    """ 
    Check if the B page appears before the A page, in which case it isn't valid
    """
    for A, B in rules:
        if A in instruction and B in instruction:
            index_a = instruction.index(A)
            index_b = instruction.index(B)
            if index_b < index_a:
                return False
            
    return True



def find_valid_order(instruction, rules):
    """
    Try to find the valid order for the instruction using backtracking.
    """
    # Base case: If instruction is of length 1, it's trivially valid.
    if len(instruction) == 1:
        return instruction

    # Try placing each element in the order
    for i in range(len(instruction)):
        current_instruction = instruction[:i] + instruction[i+1:]  # Remove the element to try placing it later
        
        # Check if the rest of the instruction is valid
        if is_order_valid(current_instruction, rules):
            # Try placing the current element at the front
            ordered = find_valid_order(current_instruction, rules)
            if ordered is not None:
                return [instruction[i]] + ordered

    return None  # Return None if no valid ordering is found


def sort_me(update, rules):
    i = 0
    while i != len(update):
        i = len(update)
        for rule in rules:
            A, B = rule[0], rule[1]
            # Value check
            if A not in update or B not in update:
                continue
            first_page = update.index(A)
            second_page = update.index(B)
            if first_page > second_page:
                i -= 1
                update.pop(first_page)
                update.insert(second_page, A)

    return update

def part_1():
    total = 0
    valid_updates = []
    for update in updates:
        if (is_order_valid(update, rules)):
            total+=1
            valid_updates.append(update)
    return sum([update[len(update)//2] for update in valid_updates])

def part_2():

    total = 0
    invalid_updates= []
    
    # Loop the instructions and check validity
    for update in updates:
        if not is_order_valid(update, rules):
            total += 1
            invalid_updates.append(update)
 
    # Loop the invalid instructions to get the correct orders
    ordered_updates = []
    for update in invalid_updates:
        ordered_update = sort_me(update, rules)
        if ordered_update:
            ordered_updates.append(ordered_update)

    return sum([update[len(update) // 2] for update in ordered_updates])

parse_data("Day5Input.txt")
result = part_1()
print(f"Part 1 = {part_1()}")
print(f"part 2 = {part_2()}")
