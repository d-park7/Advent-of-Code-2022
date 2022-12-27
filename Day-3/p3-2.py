# Day 3 part 2
# Rucksack reorganization
from string import ascii_lowercase
from string import ascii_uppercase


def generate_points_map():
    point_map = dict()
    idx = 1
    for char in ascii_lowercase:
        point_map[char] = idx 
        idx += 1

    for char in ascii_uppercase:
        point_map[char] = idx
        idx += 1

    return point_map


def calculate_points(groups: list):
    point_map = generate_points_map()
    points = 0
    counter = 0
    # TODO: figure out what is wrong with this loop
    for elf in groups:
        if (counter + 1) % 3 == 0:
            for x in groups[counter - 2]:
                for y in groups[counter - 1]:
                    for z in groups[counter]:
                        if x == y and x == z and y == z:
                            points += int(point_map.get(x))
        counter += 1

    return points


if __name__ == "__main__":
    with open('Day-3/input.txt') as file:
        groups = []
        for line in file:
            line = line.strip()
            groups.append([line])
            
        points = calculate_points(groups)
        print(points)
