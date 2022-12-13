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
    return (h.x + 1 == t.x or h.x - 1 == t.x) and (h.y + 1 == t.y or h.y - 1 == t.y)

#   O 
# O X O
#   O
def straight_adjacent(h: Point, t: Point):
    if (h.x == t.x) and (h.y + 1 == t.y or h.y - 1 == t.y):
        return True
    elif (h.y == t.y) and (h.x - 1 == t.x or h.x + 1 == t.x):
        return True
    
    return False


def move_rope(direction: str, moves: int):
    pass

test_list = [
    Point(1, 0),
    Point(1, 1),
    Point(0, 1),
    Point(-1, 1),
    Point(-1, 0),
    Point(-1, -1),
    Point(0, -1),
    Point(1, -1),
]


if __name__ == "__main__":
    visited = dict()
    head = Point(0, 0)
    tail = Point(0, 0)
    visited[tail] = True

    # Update current point as the head moves, update tail and add to dictionary of visited points
    with open('test-input.txt', 'rt') as file:
        for line in file.read().splitlines():
            tok = line.split(sep=' ')
            direction = tok[0]
            moves = int(tok[1])
            # move_rope(direction, moves)

    for p in test_list:
        if diagonal_adjacent(head, p):
            print(f"Diagonally adjacent point {p}")
        elif straight_adjacent(head, p):
            print(f"Straight adjacent {p}")

    print(f"Number of locations visited: {len(visited)}")
