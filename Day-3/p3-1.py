# Day 3 part 1
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


def calculate_points(duplicates: list):
    point_map = generate_points_map()
    points = 0
    for char in duplicates:
        points += int(point_map.get(char))

    return points


if __name__ == "__main__":
    with open('Day-3/input.txt') as file:
        duplicates = list()
        for line in file:
            line = line.strip()
            first_half = line[:len(line)//2]
            second_half = line[len(line)//2:]

            previous_appended_char = None
            for x in first_half:
                for y in second_half:
                    if x == y and x != previous_appended_char:
                        previous_appended_char = x
                        duplicates.append(x)
            
        points = calculate_points(duplicates)
        print(points)
