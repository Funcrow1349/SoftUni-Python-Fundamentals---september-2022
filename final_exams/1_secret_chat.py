concealed_message = input()
while True:
    command = input()
    if command == "Reveal":
        break
    instructions = command.split(":|:")
    action = instructions[0]
    if action == "InsertSpace":
        index = int(instructions[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif action == "Reverse":
        substring = instructions[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1) + substring[::-1]
            print(concealed_message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = instructions[1]
        replacement = instructions[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
print(f"You have a new text message: {concealed_message}")