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


# used Mark's solution bc mine was terrible
def calculate_points(rucksacks: list):
    point_map = generate_points_map()
    points = 0

    for index in range(0, len(rucksacks), 3):
        set1 = set()
        set2 = set()
        set3 = set()
        
        for letter in rucksacks[index]:
            set1.add(letter)
        for letter in rucksacks[index + 1]:
            set2.add(letter)
        for letter in rucksacks[index + 2]:
            set3.add(letter)

        result = set1.intersection(set2, set3)
        for letter in result:
            points += int(point_map.get(letter))

    return points


if __name__ == "__main__":
    with open('Day-3/input.txt') as file:
        rucksacks = file.read().splitlines()
        points = calculate_points(rucksacks)
        print(points)
