""" 
DAY 5: Supply Stacks (Part 2)
"""
from main import *


if __name__ == "__main__":
    stack = initialize_stack(input_stack)
    procedures = read_input('input.txt')

    # Move QTY # of items at src stack to dest stack
    for qty, src, dest in procedures:
        temp_stack = deque()
        for i in range(0, qty):
            # Temp stack to hold bulk move
            temp_stack.append(stack[src].pop())
        
        # Place crates in original order
        while len(temp_stack) != 0:
            stack[dest].append(temp_stack.pop())
    
    print_stacks_top(stack)
