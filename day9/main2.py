# --- Day 9: Rope Bridge (Part 2)---

from dataclasses import dataclass

ROPE_LENGTH = 10

@dataclass(eq=True)
class Point:
    x: int
    y: int

    # Must be implemented to store class into sets/dicts properly
    def __hash__(self) -> int:
        return hash((self.x, self.y))
        
    def point_dist(self, other) -> int:
        return self.x - other.x, self.y - other.y
        
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

def diagonal_adjacent(h: Point, t: Point):
    diff_x = abs(h.x - t.x)
    diff_y = abs(h.y - t.y)

    return (diff_x >= 1 and diff_y >= 1)

def straight_adjacent(h: Point, t: Point):
    diff_x = abs(h.x - t.x)
    diff_y = abs(h.y - t.y)

    return (diff_x == 0 and diff_y >= 1) or (diff_x >= 1 and diff_y == 0)

# If any part of x or y is greater than 1
def not_adjacent(h: Point, t: Point):
    return abs(h.x - t.x) > 1 or abs(h.y - t.y) > 1

ROPE = [Point(0, 0) for _ in range(ROPE_LENGTH)]
visited = set()

def move_rope(dx, dy, j):

    # 16 potential cases (4 cardinal directions + (4 diagonals * 2 permutations) + 4 (2, 2) variations)

    # Cases where distance is just a cardinal direction (N,E,S,W)
    vec = Point(0, 0)

    if dy == 0 and dx < -1:  # Tail is left 2 of head
        vec = Point(1, 0)
    elif dy == 0 and dx > 1: # Tail is right 2 of head
        vec = Point(-1, 0)
    elif dx == 0 and dy < -1:
        vec = Point(0, 1)
    elif dx == 0 and dy > 1:
        vec = Point(0, -1)

    
    # Diagonals
    elif dy > 1 and dx > 0:   # Tail right 1 up 2 (also catches (2, 2) cases)
        vec = Point(-1, -1)

    elif dy < -1 and dx > 0:  # Tail right 1 down 2
        vec = Point(-1, 1)

    elif dy < -1 and dx < 0:  # Tail left 1, down 2
        vec = Point(1,  1)

    elif dy > 1 and dx < 0:   # Tail left 1, up 2
        vec = Point(1, -1)

    elif dy > 0 and dx > 1:   # Tail up 1, right 2
        vec = Point(-1, -1)

    elif dy < 0 and dx > 1:   # Tail down 1, right 2
        vec = Point(-1, 1)

    elif dy < 0 and dx < -1:  # Tail down 1, left 2
        vec = Point(1, 1)

    elif dy > 0 and dx < -1:  # Tail up 1, left 2
        vec = Point(1, -1)

    # Move current point to correct position
    ROPE[j] += vec


if __name__ == "__main__":
    move_map = {'D': (0, -1), 'U': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

    # Update current point as the head moves, update tail and add to dictionary of visited points
    data = []
    with open('input.txt', 'rt') as file:
        for line in file.read().splitlines():
            tok = line.split(sep=' ')
            data.append((tok[0], int(tok[1])))
    
    
    for val in data:
        num_moves = val[1]
        direction = val[0]
        for i in range(num_moves):
            # Move the head to new position first, then have next rope parts follow
            ROPE[0].x += move_map[direction][0]
            ROPE[0].y += move_map[direction][1]

            for j in range(1, ROPE_LENGTH):  
                # Get distance of two rope segments
                dx, dy = ROPE[j].point_dist(ROPE[j-1])
                move_rope(dx, dy, j)
        
            visited.add(tuple((ROPE[9].x, ROPE[9].y)))

    print(f"Number of locations visited: {len(visited)}")
