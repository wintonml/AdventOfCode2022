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


def part_one():
    f = open('EncryptedStrategyGuide.txt', 'r')
    content = f.read()
    games = content.split("\n")

    elf_one_points = 0
    elf_two_points = 0

    for game in games:
        elf_one, elf_two = game.split(' ', 1)
        elf_one_shape = elf_one_dict[elf_one]
        elf_two_shape = elf_two_dict[elf_two]
        results = match_result(elf_one_shape, elf_two_shape)

        elf_one_points += results[0]
        elf_two_points += results[1]

    print(f"Elf one: {elf_one_points}")
    print(f"Elf two: {elf_two_points}")

    print(f"Total points: {elf_one_points + elf_two_points}")


def part_two():
    return True


def match_result(player_one_shape, player_two_shape):
    player_one_value = ShapePoints[player_one_shape].value
    player_two_value = ShapePoints[player_two_shape].value
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
    else:
        player_one_points = player_one_value + ResultsPoints.Win.value
        player_two_points = player_two_value + ResultsPoints.Loss.value

    return player_one_points, player_two_points


if __name__ == '__main__':
    part_one()