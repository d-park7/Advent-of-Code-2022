# Day 1 Part 2: Calorie Counting

# Find sum of calories of top 3

calories = 0
total_calories = 0
calories_per_elf = []

with open('Day 1/input.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        if line == '':
            calories_per_elf.append(calories)
            calories = 0
        if line != '':
            calories += int(line)
    
calories_per_elf.sort(reverse=True)

for elf in calories_per_elf[0:3]:
    total_calories += elf

print(total_calories)
