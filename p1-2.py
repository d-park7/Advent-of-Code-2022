# Day 1 Part 2: Calorie Counting

# Find sum of calories of top 3

calories = 0
top_three_caloires = [0, 0, 0]

with open('input.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        if line == '':
            third_max = top_three_caloires[2]
            if third_max < calories:
                top_three_caloires[2] = calories   
                top_three_caloires.sort()
            calories = 0
        if line != '':
            calories += int(line)
        print(top_three_caloires)