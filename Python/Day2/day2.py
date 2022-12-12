from enum import Enum


class ShapePoints(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class ResultsPoints(Enum):
    Loss = 0
    Draw = 3
    Win = 6


elf_one_dict = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
}

elf_two_dict = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

desired_result_dict = {
    "X": "Loss",
    "Y": "Draw",
    "Z": "Win",
}


def part_one():
    print("Part 1 Challenge")
    complete_challenge(1)


def part_two():
    print("\nPart 2 Challenge")
    complete_challenge(2)


def complete_challenge(challenge_number):
    games = get_games()

    elf_one_points = 0
    elf_two_points = 0

    for game in games:
        elf_one, column_two = game.split(' ', 1)
        elf_one_shape = elf_one_dict[elf_one]

        if challenge_number == 1:
            elf_two_shape = elf_two_dict[column_two]
            results = match_result(elf_one_shape, elf_two_shape)
        else:
            result = desired_result_dict[column_two]
            results = match_result(elf_one_shape, game_result=result)

        elf_one_points += results[0]
        elf_two_points += results[1]

    print(f"Elf one: {elf_one_points}")
    print(f"Elf two: {elf_two_points}")


def get_games():
    f = open('EncryptedStrategyGuide.txt', 'r')
    content = f.read()
    return content.split("\n")


def find_player_two_shape(player_one_value, game_result):
    if game_result == "Draw":
        player_two_value = player_one_value
    elif game_result == "Win":
        potential_value = player_one_value + 1
        player_two_value = potential_value if potential_value != 4 else 1
    elif game_result == "Loss":
        potential_value = player_one_value - 1
        player_two_value = potential_value if potential_value != 0 else 3
    return player_two_value


def match_result(player_one_shape, player_two_shape=-100, game_result=None):
    player_one_value = ShapePoints[player_one_shape].value
    if game_result is None:
        player_two_value = ShapePoints[player_two_shape].value
    else:
        player_two_value = find_player_two_shape(player_one_value,
                                                 game_result)
    player_difference = player_two_value - player_one_value

    # Draw condition
    if player_difference == 0:
        player_one_points = player_one_value + ResultsPoints.Draw.value
        player_two_points = player_two_value + ResultsPoints.Draw.value

    # Win condition is difference of 1 or -2
    elif player_difference in (1, -2):
        player_one_points = player_one_value + ResultsPoints.Loss.value
        player_two_points = player_two_value + ResultsPoints.Win.value

    # Lose condition is difference of -1 or 2
    elif player_difference in (-1, 2):
        player_one_points = player_one_value + ResultsPoints.Win.value
        player_two_points = player_two_value + ResultsPoints.Loss.value

    return player_one_points, player_two_points


if __name__ == '__main__':
    part_one()
    part_two()
