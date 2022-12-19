""" 
Day 11: Monkey In the Middle (Part 1 & 2 -> check fn.py)

https://adventofcode.com/2022/day/11
"""
from fn import *

for rounds in range(NUM_ROUNDS):
  # Go through each monkey's turn (round)
  for i in range(0, NUM_MONKEYS, 1): 
      # Go through each item per monkey
      for item in monkeys[i]:
        funcs[i](item)     # Run monkey's function
        counts[i] += 1     # Update # of inspected items
        
      # Clean out list when all items have been inspected
      monkeys[i].clear()
    
act = [i for i in counts.values()]
act = sorted(act, reverse=True)
print(f"Monkey business level after 20 rounds: {act[0] * act[1]}")
  
      
  
      
    
  
      
      