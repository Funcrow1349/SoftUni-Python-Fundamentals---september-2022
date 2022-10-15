line_of_strings = input().split()
current_command = input()
while current_command != "3:1":
    current_command = current_command.split()
    if current_command[0] == "merge":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        word_to_add = ""
        if start_index < 0:
            start_index = 0
        if end_index >= len(line_of_strings):
            end_index = len(line_of_strings) -1
        for char in range(start_index, end_index + 1):
            word_to_add += line_of_strings[char]
        line_of_strings.insert(start_index, word_to_add)
        for index in range(start_index, end_index + 1):
            line_of_strings.pop(start_index + 1)
    elif current_command[0] == "divide":
        item_to_remove = int(current_command[1])
        item_position = int(current_command[1])
        partitions = int(current_command[2])
        element_from_list = line_of_strings[item_position]
        max_length_of_element = len(element_from_list) // partitions
        elements_done = 0
        word_to_add = ""
        for index, letter in enumerate(element_from_list):
            word_to_add += letter
            if len(element_from_list) % partitions != 0 and elements_done == partitions - 1:
                item_position += 1
                word_to_add += element_from_list[(index + 1): len(element_from_list) + 1]
                line_of_strings.insert(item_position, word_to_add)
                break
            elif (index + 1) % max_length_of_element == 0:
                item_position += 1
                line_of_strings.insert(item_position, word_to_add)
                word_to_add = ""
                elements_done += 1
        line_of_strings.remove(line_of_strings[item_to_remove])
    current_command = input()
print(" ".join(line_of_strings))
