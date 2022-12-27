# Day 2 Part 2: Rock paper scissors

# Find total points


point_mapping = {
        'AX': 3,
        'AY': 4,
        'AZ': 8,
        'BX': 1,
        'BY': 5,
        'BZ': 9,
        'CX': 2,
        'CY': 6,
        'CZ': 7
}


def calculate_points(play_book: list):
    points = 0
    for play in play_book:
        points += point_mapping[play]
    return points


if __name__ == "__main__":
    with open('Day-2/input.txt') as file:
        play_book = []
        for line in file:
            line = line.strip()
            play_book.append(line.replace(' ', ''))
    
        points = calculate_points(play_book)
        print(points)
