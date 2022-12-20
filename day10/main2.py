""" 
Day 10: Cathode-Ray Tube (Part 2)

Link: https://adventofcode.com/2022/day/10
"""

instructions = []
cycles = dict() 

with open('input.txt', 'r') as file:
    for line in file.read().splitlines():
      instructions.append(line)   

# Check if the sprite is overlapping with drawing position
def check_overlap(draw_pos: int, sc: int):
  l = sc-1
  r = sc+1
  return (l == draw_pos or sc == draw_pos or r == draw_pos)
  
cycle = 1
X = 1
for i in instructions:
  if 'noop' == i:
    cycles[cycle] = X % 40
    cycle += 1
    continue
  else:
    val = int(i.split()[1])
    
    # Set val before execution
    cycles[cycle] = X % 40
    
    # Increment to next cycle
    cycle += 1
    
    
    # Set before 2nd phase of execution
    cycles[cycle] = X % 40
    
    # Increment value after done
    X += val
    
    # Increment once again
    cycle += 1
    
    continue
  

# Use results from part 1 to print drawing for part 2 (using cycle vals)
# TODO: Bugged -> current doesn't print the 1st column correct 
#   (can deduce correct answer)
row = 1
for k, v in cycles.items():
  if check_overlap((k-1) % 40, v):
    print('#', end='')
  else:
    print(' ', end='')
    
  if k % 40 == 0:
    print('')
    




    
    
    
  
  

