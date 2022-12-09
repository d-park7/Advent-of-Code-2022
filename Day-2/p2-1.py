# Day 2 Part 1: Rock paper scissors

# Find total points


point_mapping = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,

        'AX': 3,
        'AY': 6,
        'AZ': 0,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 6,
        'CY': 0,
        'CZ': 3
}


def calculate_points(play_book: list):
    opponent_move = play_book[0]
    your_move = play_book[1]
    match_points = opponent_move + your_move

    points = point_mapping.get(your_move)
    points += point_mapping.get(match_points)
    return points


if __name__ == "__main__":
    with open('Day-2/input.txt') as file:
        points = 0
        for line in file:
            line = line.replace('\n', '')
            play_book = line.split(' ')
            points += calculate_points(play_book)
    
        print(points)
