# --- Day 9: Rope Bridge ---
from dataclasses import dataclass

@dataclass(eq=True)
class Point:
    x: int
    y: int

    # Must be implemented to store class into sets/dicts properly
    def __hash__(self) -> int:
        return hash((self.x, self.y))


# O   O
#   X 
# O   O
def diagonal_adjacent(h: Point, t: Point):
    diff_x = abs(h.x - t.x)
    diff_y = abs(h.y - t.y)

    return (diff_x >= 1 and diff_y >= 1)

#   O 
# O X O
#   O
def straight_adjacent(h: Point, t: Point):
    diff_x = abs(h.x - t.x)
    diff_y = abs(h.y - t.y)

    return (diff_x == 0 and diff_y >= 1) or (diff_x >= 1 and diff_y == 0)

# If any part of x or y is greater than 1
def not_adjacent(h: Point, t: Point):
    return abs(h.x - t.x) > 1 or abs(h.y - t.y) > 1

visited = dict()

def move_rope(direction: str, moves: int, head, tail):
    dy = 0
    dx = 0
    if direction == 'L':
        dx = -1
    elif direction == 'R':
        dx = 1
    elif direction == 'U':
        dy = 1
    elif direction == 'D':
        dy = -1

    for i in range(moves):
        head.x = head.x + dx
        head.y = head.y + dy
        # print(f"Head {head} | Tail {tail}")

        if not_adjacent(head, tail):
            if straight_adjacent(head, tail):
                # Move tail in just x or just y direction
                diff_X = 0
                diff_Y = 0
                if direction == 'R':
                    diff_X = head.x - tail.x - 1
                elif direction == 'L':
                    diff_X = head.x - tail.x + 1
                elif direction == 'U':
                    diff_Y = head.y - tail.y - 1
                elif direction == 'D':
                    diff_Y = head.y - tail.y + 1
                
                tail.x += diff_X
                tail.y += diff_Y

                print(tail)

                if tail not in visited:
                    visited[Point(tail.x, tail.y)] = True

            elif diagonal_adjacent(head, tail):
                # Move tail in both X and Y directions
                if direction == 'R':
                    diff_Y = head.y - tail.y
                    diff_X = head.x - tail.x - 1
                elif direction == 'L':
                    diff_Y = head.y - tail.y
                    diff_X = head.x - tail.x + 1
                elif direction == 'U':
                    diff_Y = head.y - tail.y - 1
                    diff_X = head.x - tail.x
                elif direction == 'D':
                    diff_Y = head.y - tail.y + 1
                    diff_X = head.x - tail.x
                
                tail.x += diff_X
                tail.y += diff_Y
                
                if tail not in visited:
                    visited[Point(tail.x, tail.y)] = True

                print(tail)


if __name__ == "__main__":
    head = Point(0, 0)
    tail = Point(0, 0)
    visited[Point(tail.x, tail.y)] = True

    # Update current point as the head moves, update tail and add to dictionary of visited points
    with open('input.txt', 'rt') as file:
        for line in file.read().splitlines():
            tok = line.split(sep=' ')
            direction = tok[0]
            moves = int(tok[1])
            move_rope(direction, moves, head, tail)

    print(f"Number of locations visited: {len(visited)}")
