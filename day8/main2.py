"""
Day 8: Treetop Tree House (Part 2)

Link: https://adventofcode.com/2022/day/8
"""

grid = []
with open('input.txt', 'rt') as file:
    for line in file.read().splitlines():
        grid.append([n for n in line])


def check_scenic_score(row, col):
    curr_tree = grid[row][col]
    l_score, r_score, u_score, d_score = 0, 0, 0, 0

    for right in range(col+1, len(grid[row])):
        if curr_tree <= grid[row][right]:
            r_score += 1
            break
        else:
            r_score += 1
    for left in range(col-1, -1, -1):
        if curr_tree <= grid[row][left]:
            l_score += 1
            break
        else:
            l_score += 1
    for up in range(row-1, -1, -1):
        if curr_tree <= grid[up][col]:
            u_score += 1
            break
        else:
            u_score += 1
    for down in range(row+1, len(grid[row])):
        if curr_tree <= grid[down][col]:
            d_score += 1
            break
        else:
            d_score += 1

    score = (u_score * l_score * d_score * r_score)
    return score

if __name__ == "__main__":

    top_spots = {}

    # Start and end indices are 2nd to outer ring
    for row in range(1, len(grid)-1):
        c = grid[row]
        for col in range(1, len(c)-1):
            top_spots.setdefault(check_scenic_score(row, col), f"({row}, {col})")
    
    print(f"Highest scenic score: {max(top_spots)} at {top_spots[max(top_spots)]}")

    

