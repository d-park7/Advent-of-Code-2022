""" 
Day 2: Rock Paper Scissors

Link to Problem: https://adventofcode.com/2022/day/2
"""
opp_move = {
    'A': 'R',
    'B': 'P',
    'C': 'S'
}

player_move = {
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}

player_choice = {
    'R': 1,
    'P': 2,
    'S': 3,
}

result_map = {
    'W': 6,
    'D': 3,
    'L': 0,
}

def calculate_result_points(opponent, player):
    r = opponent + player

    if r == 'RR' or r == 'PP' or r == 'SS':
        result = 'D'
    elif r == 'RP' or r == 'PS' or r == 'SR':
        result = 'W'
    elif r == 'PR' or r == 'SP' or r == 'RS':
        result = 'L'

    return result_map[result]

def calculate_round_points(opponent, player):
    shape_pts = player_choice[player]
    result_pts = calculate_result_points(opponent, player)
    return shape_pts + result_pts


if __name__ == "__main__":
    with open('data.txt', 'rt') as file:
        moves = file.read().splitlines()
    
    total_points = 0

    for move in moves:
        opponent = opp_move[move[0]]
        player = player_move[move[2]]

        total_points += calculate_round_points(opponent, player)

    print(f"Total Points: {total_points}")
