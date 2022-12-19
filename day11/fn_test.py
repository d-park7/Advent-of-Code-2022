from math import prod
monkeys = dict()
NUM_ROUNDS = 20
NUM_MONKEYS = 4
FILE_NAME = 'input_test.txt'

def throw(num: int, dn: int, tt: int, ft: int):
  n = int(num // 3)  
  if n % dn == 0:
    monkeys[tt].append(n)
  else:
    monkeys[ft].append(n)
    
# Returns the monkey index
def m0(old: int) -> int:
  new = old * 19
  throw(new, 23, 2, 3)

def m1(old: int) -> int:
  new = old + 6
  throw(new, 19, 2, 0)
  
def m2(old: int) -> int:
  new = old * old
  throw(new, 13, 1, 3)
  
def m3(old: int) -> int:
  new = old + 3
  throw(new, 17, 0, 1)
  
funcs = {
  0: m0,
  1: m1,
  2: m2,
  3: m3,
}

counts = {i: 0 for i in range(4)}