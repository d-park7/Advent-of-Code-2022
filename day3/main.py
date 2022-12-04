"""
Day 3: Rucksack Reorganization

Link: https://adventofcode.com/2022/day/3

"""

# Calculate priority value of letter as listed in instructions
def calculate_priority(letter: str):
    if letter.isupper():
        priority_val = ord(letter) - ord("A") + 27
    else:
        priority_val = ord(letter) - ord("a") + 1

    return priority_val


if __name__ == "__main__":

    with open("input.txt", "rt") as file:
        rucksacks = file.read().splitlines()

    # Use a set for each rucksack to keep track of unique items in 1st half of string
    #  Find matching item in set when iterating through 2nd half of string
    priority_sum = 0
    for rucksack in rucksacks:
        item_types = set()
        for index, val in enumerate(rucksack):
            if index < len(rucksack) / 2:
                item_types.add(val)
            else:
                if val in item_types:
                    priority_sum += calculate_priority(val)
                    break

    print(f"Priority sum: {priority_sum}")
