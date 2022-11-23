initial_string = input()
while True:
    command = input()
    if command == "Travel":
        break
    instruction = command.split(":")
    action = instruction[0]
    if action == "Add Stop":
        index = int(instruction[1])
        destination = instruction[2]
        if 0 <= index < len(initial_string):
            initial_string = initial_string[:index] + destination + initial_string[index:]
        print(initial_string)
    elif action == "Remove Stop":
        start_index = int(instruction[1])
        end_index = int(instruction[2])
        if 0 <= start_index < len(initial_string) and 0 <= end_index < len(initial_string):
            initial_string = initial_string[:start_index] + initial_string[end_index + 1:]
        print(initial_string)
    elif action == "Switch":
        old_string = instruction[1]
        new_string = instruction[2]
        if old_string in initial_string:
            initial_string = initial_string.replace(old_string, new_string)
        print(initial_string)
print(f"Ready for world tour! Planned stops: {initial_string}")