""" 
Day 2: Rock Paper Scissors (Part 2)

Link to Problem: https://adventofcode.com/2022/day/2
"""
opp_move = {
    'A': 'R',
    'B': 'P',
    'C': 'S'
}

player_move = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W'
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


def calculate_round_points(opponent, player):
    player_mv = ''

    if player == 'L':
        if opponent == 'R':
            player_mv = 'S'
        elif opponent == 'P':
            player_mv = 'R'
        elif opponent == 'S':
            player_mv = 'P'
    elif player == 'D':
        player_mv = opponent
    elif player == 'W':
        if opponent == 'R':
            player_mv = 'P'
        elif opponent == 'P':
            player_mv = 'S'
        elif opponent == 'S':
            player_mv = 'R'

    return result_map[player] + player_choice[player_mv]


if __name__ == "__main__":
    with open('data.txt', 'rt') as file:
        moves = file.read().splitlines()
    
    total_points = 0

    for move in moves:
        opponent = opp_move[move[0]]
        player = player_move[move[2]]
        total_points += calculate_round_points(opponent, player)

    print(total_points)
