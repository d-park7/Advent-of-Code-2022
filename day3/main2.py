"""
Day 3: Rucksack Reorganization (Part 2)

Link: https://adventofcode.com/2022/day/3
"""
from main import calculate_priority

if __name__ == "__main__":

    with open("input.txt", "rt") as file:
        rucksacks = file.read().splitlines()

    # Find intersection of 3 sets for common value
    priority_sum = 0
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

        common_set = set1.intersection(set2, set3)

        for item in common_set:
            priority_sum += calculate_priority(item)

    print(f"Priority sum: {priority_sum}")
