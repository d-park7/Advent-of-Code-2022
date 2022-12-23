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
      start = (row, col)
    elif grid[row][col] == 'E':
      end = (row, col)
      
# Set node to starting point, and then run algorithm
def travel():
  visited = []
  prio_q = []
  node = start
  
  
  
  
  
  

  
  