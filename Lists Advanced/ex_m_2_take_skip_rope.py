initial_strings = input()
numbers_list = []
non_numbers_list = []
take_list = []
skip_list = []
taken_string = ""
skipped_string = ""
for char in initial_strings:
    if char.isdigit():
        numbers_list.append(int(char))
    else:
        non_numbers_list.append(char)
for index in range(len(numbers_list)):
    if index % 2 == 0:
        take_list.append(numbers_list[index])
    else:
        skip_list.append(numbers_list[index])
for (m, n) in zip(take_list, skip_list):
    taken_characters = m
    skipped_characters = n
    taken_and_skipped_list = []
    for char in non_numbers_list:
        if taken_characters > 0:
            taken_and_skipped_list.append(char)
            taken_string += char
            taken_characters -= 1
        elif skipped_characters > 0:
            taken_and_skipped_list.append(char)
            skipped_string += char
            skipped_characters -= 1
    for item in taken_and_skipped_list:
        non_numbers_list.remove(non_numbers_list[0])
print(taken_string)

