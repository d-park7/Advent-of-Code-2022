from heapq import heappop, heappush
from dataclasses import dataclass

@dataclass
class Node:
  row: int
  col: int
  visited: bool
  
  def __init__(self, x, y, visited=False) -> None:
    self.row = x
    self.col = y
    self.visited = visited
    
  def __eq__(self, other) -> bool:
    return self.row == other.row and self.col == other.col
    

grid = []
with open('input_test.txt', 'r') as file:
  grid = [list(row) for row in file.read().splitlines()]

def height(row, col):
  letter = grid[row][col]
  if letter == 'S':
    return 0
  elif letter == 'E':
    return 26
  else:
    return ord(letter) - 97
  
  
# Get starting spots
for row in range(len(grid)):
  for col in range(len(grid[row])):
    if grid[row][col] == 'S':
      start = Node(row, col)
    elif grid[row][col] == 'E':
      end = Node(row, col)

# Start and end are nodes containing (x, y, visited) position on grid
def travel(start, end):
  pq = [] 
  heappush(pq, start)   # Push start node onto queue  
  
  while len(pq) > 0:
    curr_steps, node = heappop(pq)
    if not node.visited:
      node.visited = True
      if node == end:
        return curr_steps
      else:
        pass  # Logic for adding new neighbor nodes here

  
travel(start, end) 
  
  
  
  

  
  