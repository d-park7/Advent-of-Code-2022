""" 
DAY 5: Supply stacks

Link: https://adventofcode.com/2022/day/5


# [T]     [D]         [L]            
# [R]     [S] [G]     [P]         [H]
# [G]     [H] [W]     [R] [L]     [P]
# [W]     [G] [F] [H] [S] [M]     [L]
# [Q]     [V] [B] [J] [H] [N] [R] [N]
# [M] [R] [R] [P] [M] [T] [H] [Q] [C]
# [F] [F] [Z] [H] [S] [Z] [T] [D] [S]
# [P] [H] [P] [Q] [P] [M] [P] [F] [D]
#  1   2   3   4   5   6   7   8   9 
"""
from collections import deque

input_stack = [
    'PFMQWGRT',
    'HFR',
    'PZRVGHSD',
    'QHPBFWG',
    'PSMJH',
    'MZTHSRPL',
    'PTHNML',
    'FDQR',
    'DSCNLPH'
]

""" 
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""

test_stack = [
    'ZN',
    'MCD',
    'P',
]

def initialize_stack(stack_list):
    deque_stack = {}
    for index, item_stack in enumerate(stack_list):
        stack = deque()
        for letter in item_stack:
            stack.append(letter)
        deque_stack[index+1] = stack
    
    return deque_stack

def read_input(file_name):
    procedures = []
    with open(file_name, 'rt') as file:
        for line in file.read().splitlines():
            tokens = line.split(sep=' ')
            qty, src, dest = int(tokens[1]), int(tokens[3]), int(tokens[5])
            procedures.append((qty, src, dest))

    return procedures

def print_stacks_top(stack):
    for val in stack.values():
        print(val[-1], end='')
    print()


if __name__ == "__main__":
    stack = initialize_stack(input_stack)
    procedures = read_input('input.txt')

    # Move QTY # of items at src stack to dest stack
    for qty, src, dest in procedures:
        for i in range(0, qty): 
            stack[dest].append(stack[src].pop())
    
    print_stacks_top(stack)



            
    
