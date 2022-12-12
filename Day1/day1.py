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
    print(max_calories_carried)
    f.close()
