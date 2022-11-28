raw_activation_key = input()
while True:
    command = input()
    if command == "Generate":
        print(f"Your activation key is: {raw_activation_key}")
        break
    instructions = command.split(">>>")
    action = instructions[0]
    if action == "Contains":
        substring = instructions[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        upper_or_lower = instructions[1]
        start_index = int(instructions[2])
        end_index = int(instructions[3])
        substring = raw_activation_key[start_index:end_index]
        if upper_or_lower == "Upper":
            new_substring = substring.upper()
        elif upper_or_lower == "Lower":
            new_substring = substring.lower()
        raw_activation_key = raw_activation_key.replace(substring, new_substring)
        print(raw_activation_key)
    elif action == "Slice":
        start_index = int(instructions[1])
        end_index = int(instructions[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

