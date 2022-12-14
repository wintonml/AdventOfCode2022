import Python.HelperFile as Helper


def part_one(overlap_list):
    print("Part 1 Challenge")
    range_finder(overlap_list)


def part_two(overlap_list):
    print("\nPart 2 Challenge")
    range_finder(overlap_list, False)


def range_finder(list_of_ranges, completely_in_range=True):
    count = 0
    for overlap in list_of_ranges:
        elf_one, elf_two = overlap.split(',')
        elf_one_range = elf_one.split('-')
        elf_two_range = elf_two.split('-')

        e1_low = int(elf_one_range[0])
        e1_high = int(elf_one_range[1])
        e2_low = int(elf_two_range[0])
        e2_high = int(elf_two_range[1])
        if completely_in_range:
            if ((e1_low <= e2_low and e1_high >= e2_high) or
                    (e1_low >= e2_low and e1_high <= e2_high)):
                count += 1
                # print(f"{elf_one_range} : {elf_two_range}")
        else:
            elf_one_range = list(range(e1_low, e1_high + 1))
            elf_two_range = list(range(e2_low, e2_high + 1))
            if ((e1_low or e1_high) in elf_two_range or
                    ((e2_low or e2_high) in elf_one_range)):
                count += 1

    print(f"Total ranges overlapping: {count}")


if __name__ == '__main__':
    cleaning_areas, file = Helper.read_and_split_text("TextInput.txt", '\n')
    part_one(cleaning_areas)
    part_two(cleaning_areas)
    file.close()
