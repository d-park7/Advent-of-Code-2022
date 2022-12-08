""" 
Day 2: Rock Paper Scissors (Part 2)

Link to Problem: https://adventofcode.com/2022/day/2
"""
from main import opp_move, player_choice, result_map

player_move = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W',
}

player_win_choice = {
    'R': 'P',
    'P': 'S',
    'S': 'R',
}
player_lose_choice = {
    'R': 'S',
    'P': 'R',
    'S': 'P',
}


def calculate_round_points(opponent, player):
    player_mv = ''

    if player == 'L':
        player_mv = player_lose_choice[opponent]
    elif player == 'D':
        player_mv = opponent
    elif player == 'W':
        player_mv = player_win_choice[opponent]

    return result_map[player] + player_choice[player_mv]


if __name__ == "__main__":
    with open('data.txt', 'rt') as file:
        moves = file.read().splitlines()
    
    total_points = 0

    for move in moves:
        opponent = opp_move[move[0]]
        player = player_move[move[2]]
        total_points += calculate_round_points(opponent, player)

    print(f"Total points: {total_points}")
