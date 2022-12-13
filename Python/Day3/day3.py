import Python.HelperFile as Helper


def part_one(sack_list):
    print("Part 1 Challenge")
    priority_list = []
    for sack in sack_list:
        half_list_length = int(len(sack) / 2)
        first_compartment = sack[:half_list_length]
        second_compartment = sack[half_list_length:]
        for char in first_compartment:
            found = char in second_compartment
            if found:
                priority_list.append(find_char_value(char))
                # print(f"{char}: {find_char_value(char)}")
                break

    print(f"Total priority: {sum(priority_list)}")


def part_two(sack_list):
    print("\nPart 2 Challenge")
    priority_list = []
    for i in range(0, len(sack_list), 3):
        first_elf, second_elf, third_elf = sack_list[i], sack_list[i+1], \
                                           sack_list[i+2],
        for char in first_elf:
            if char in second_elf and char in third_elf:
                priority_list.append(find_char_value(char))
                # print(f"{char}: {find_char_value(char)}")
                break

    print(f"Total priority: {sum(priority_list)}")


def find_char_value(char):
    char_int_value = ord(char)
    return (char_int_value - ord('A') + 27 if char.isupper() else
            char_int_value - ord('a') + 1)


if __name__ == '__main__':
    sacks, file = Helper.read_and_split_text("SackContent.txt", '\n')
    part_one(sacks)
    part_two(sacks)
    file.close()
