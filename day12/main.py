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
  
  def __gt__(self, other) -> bool:
    return self.row > row or self.col > col
    
grid = []
with open('input.txt', 'r') as file:
  grid = [list(row) for row in file.read().splitlines()]

def check_bounds(row, col):
  return (row >= 0 and row < len(grid) and 
          col >= 0 and col < len(grid[0])) 
  

def height(row, col):
  letter = grid[row][col]
  if letter == 'S':
    return 0
  elif letter == 'E':
    return 26
  else:
    return ord(letter) - 97
  
def find_neighbors(row, col):
  curr_height = height(row, col)
  neighbors = []
  nb_list = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
  for pos in nb_list:
    if check_bounds(pos[0], pos[1]):
      if height(pos[0], pos[1]) <= curr_height + 1:
        neighbors.append((pos[0], pos[1]))
  
  return neighbors        
  
  
# Get starting spots 
starting_spots = []
for row in range(len(grid)):
  for col in range(len(grid[row])):
    if grid[row][col] == 'S':
      start = (row, col)
      starting_spots.append((row, col))
    elif grid[row][col] == 'E':
      end = (row, col)
    elif grid[row][col] == 'a':
      starting_spots.append((row, col))


# Node is a tuple (row, col)
def travel(start, end):
  pq = [] 
  heappush(pq, (0, start))   # Push start node onto queue  
  visited = set()
   
  while len(pq) > 0:
    curr_steps, node = heappop(pq)
    if node not in visited:
      visited.add(node)
      if node == end:
        return curr_steps
      else:
        for nd in find_neighbors(node[0], node[1]):
          heappush(pq, (curr_steps+1, nd))

  
steps = travel(start, end) 
print(steps)
  
# Part 2, run algorithm with starting spots of a or S
steps_list = []
for start_pos in starting_spots:
  steps = travel(start_pos, end)
  
  # Some paths may return None types, skip if None
  if steps is not None:
    steps_list.append(steps)

print(min(steps_list))
  
  

  
  