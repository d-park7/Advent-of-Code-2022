"""
Day 8: Treetop Tree House

Link: https://adventofcode.com/2022/day/8
"""
grid = []
with open('input.txt', 'rt') as file:
    for line in file.read().splitlines():
        grid.append([n for n in line])

def check_direction(dir, row, col):
    curr_tree = grid[row][col]
    visible = True
    if dir == 'R':
        for right in range(col+1, len(grid[row])):
            if curr_tree <= grid[row][right]:
                visible = False
                break
    elif dir == 'L':
        for left in range(col-1, -1, -1):
            if curr_tree <= grid[row][left]:
                visible = False
                break
    elif dir == 'U':
        for up in range(row-1, -1, -1):
            if curr_tree <= grid[up][col]:
                visible = False
                break
    elif dir == 'D':
        for down in range(row+1, len(grid[row])):
            if curr_tree <= grid[down][col]:
                visible = False
                break
    return visible


def check_visible(row, col):
    return (
        check_direction('R', row, col) or
        check_direction('L', row, col) or
        check_direction('U', row, col) or
        check_direction('D', row, col)
    )

if __name__ == "__main__":

    # Initialize visible trees to # of edge trees
    trees_visible = (len(grid) * 4) - 4

    # Start and end indices are 2nd to outer ring
    for row in range(1, len(grid)-1):
        c = grid[row]
        for col in range(1, len(c)-1):
            if check_visible(row, col):
                trees_visible += 1

    print(f"Trees visible from outer edge: {trees_visible}")
    

