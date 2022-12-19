from math import prod
# PART = 'p1'    # Uncomment this line to solve for part 1
PART = 'p2'

if PART == 'p1':
  NUM_ROUNDS = 20
else:
  NUM_ROUNDS = 10000

NUM_MONKEYS = 8
FILE_NAME = 'input.txt'
monkeys = {i: [] for i in range(NUM_MONKEYS)}
counts = {i: 0 for i in range(NUM_MONKEYS)}

# Read input
with open(FILE_NAME, 'r') as file:
  for line in file.read().splitlines():
    if line.startswith('Monkey'):
      curr = int(line[len(line)-2])
    elif 'Starting items' in line:
      itms = [int(i) for i in line[line.index(':')+2:].split(', ')]
      monkeys[curr] = itms

# Create an arbitrary large number to modulo all numbers (to reduce size)
super_list = []
for value_list in monkeys.values():
  super_list += value_list
mod = prod(super_list)


# Does value checks and throws to another monkey
def throw(num: int, dn: int, tt: int, ft: int):
  
  # Modulo should keep numbers within reasonable bounds
  n = int(num//3) if PART == 'p1' else num % mod
  
  # Modulo number 
  if n % dn == 0:
    monkeys[tt].append(n)
  else:
    monkeys[ft].append(n)
    
# Create mapped functions for each monkey
def m0(old: int) -> int:
  new = old * 7
  throw(new, 5, 1, 6)

def m1(old: int) -> int:
  new = old * old
  throw(new, 17, 2, 5)
  
def m2(old: int) -> int:
  new = old + 8
  throw(new, 7, 4, 3)
  
def m3(old: int) -> int:
  new = old + 4
  throw(new, 13, 0, 7)
  
def m4(old: int) -> int:
  new = old + 3
  throw(new, 19, 7, 3)
  
def m5(old: int) -> int:
  new = old + 5
  throw(new, 3, 4, 2)
  
def m6(old: int) -> int:
  new = old + 7
  throw(new, 11, 1, 5)

def m7(old: int) -> int:
  new = old * 3
  throw(new, 2, 0, 6)

funcs = {
  0: m0,
  1: m1,
  2: m2,
  3: m3,
  4: m4,
  5: m5,
  6: m6,
  7: m7,
}
