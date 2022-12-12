def part_one():
    f = open('PartOneInput.txt', 'r')
    content = f.read()
    elves = content.split("\n\n")
    elf_calories = []

    for elf in elves:
        calories_carried = elf.split("\n")
        calories_carried = (map(int, calories_carried))
        elf_calories.append(sum(calories_carried))

    max_calories_carried = max(elf_calories)
    print(f"Max amount of calories: {max_calories_carried}")

    f.close()

    return elf_calories


def part_two():
    top_elves_of_interest = 3
    calories_carried = part_one()
    calories_carried.sort(reverse=True)  # descending order

    top_elves = calories_carried[0:top_elves_of_interest]
    print(f"Max calories of top {top_elves_of_interest}: {sum(top_elves)}")


if __name__ == '__main__':
    part_two()
