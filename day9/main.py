# --- Day 9: Rope Bridge ---
from dataclasses import dataclass

@dataclass(eq=True)
class Point:
    x: int
    y: int

    # Must be implemented to store class into sets/dicts properly
    def __hash__(self) -> int:
        return hash((self.x, self.y))


# Holds a pair of x,y coordinates and visited status
visited = dict()

if __name__ == "__main__":
    
    head = Point(0, 0)
    tail = Point(0, 0)
    visited[tail] = True

    # Update current point as the head moves, update tail and add to dictionary of visited points
    