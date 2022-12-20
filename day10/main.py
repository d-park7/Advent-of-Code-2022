""" 
Day 10: Cathode-Ray Tube (Part 1)

Link: https://adventofcode.com/2022/day/10
"""

instructions = []
cycles = dict()   # Store value at each cycle

with open('input.txt', 'r') as file:
    for line in file.read().splitlines():
      instructions.append(line)   


cycle = 1
X = 1
for i in instructions:
  if 'noop' == i:
    cycles[cycle] = X
    cycle += 1
    continue
  else:
    val = int(i.split()[1])
    
    # Set val before execution
    cycles[cycle] = X
    
    # Increment to next cycle
    cycle += 1
    
    # Set before 2nd phase of execution
    cycles[cycle] = X
    
    # Increment value after done
    X += val
    
    # Increment once again
    cycle += 1
    continue
  
sigsum = 0
for k, v in cycles.items():
  if k % 40 == 20:
    print(k, v)
    sigsum += (k *  v)
    
print("Part 1 signal strength:", sigsum)

    
    
    
  
  

