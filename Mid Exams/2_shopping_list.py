list_of_groceries = input().split("!")
while True:
    command = input()
    if command == "Go Shopping!":
        break
    current_command = command.split()
    if current_command[0] == "Urgent":
        item = current_command[1]
        if item not in list_of_groceries:
            list_of_groceries.insert(0, item)
    elif current_command[0] == "Unnecessary":
        item = current_command[1]
        if item in list_of_groceries:
            list_of_groceries.remove(item)
    elif current_command[0] == "Correct":
        old_item = current_command[1]
        new_item = current_command[2]
        if old_item in list_of_groceries:
            index_of_old_item = list_of_groceries.index(old_item)
            list_of_groceries[index_of_old_item] = new_item
    elif current_command[0] == "Rearrange":
        item = current_command[1]
        if item in list_of_groceries:
            list_of_groceries.remove(item)
            list_of_groceries.append(item)

print(", ".join(list_of_groceries))
