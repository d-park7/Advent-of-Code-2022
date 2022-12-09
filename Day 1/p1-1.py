# Day 1 Part 1: Calorie Counting

# Find max

calories = 0
max = 0

with open('Day 1/input.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        if line == '':
            if max < calories:
                max = calories   
            calories = 0
        elif line != '':
            calories += int(line)


print(max)
