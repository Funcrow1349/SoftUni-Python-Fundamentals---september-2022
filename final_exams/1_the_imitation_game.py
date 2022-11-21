encrypted_message = input()
while True:
    command = input()
    if command == "Decode":
        break
    instruction = command.split("|")
    action = instruction[0]
    if action == "Move":
        nr_of_letters = int(instruction[1])
        counter = int(instruction[1])
        for letter in encrypted_message:
            encrypted_message += letter
            counter -= 1
            if counter == 0:
                break
        encrypted_message = encrypted_message[nr_of_letters::]
    elif action == "Insert":
        index = int(instruction[1])
        char_to_insert = instruction[2]
        encrypted_message = encrypted_message[:index] + char_to_insert + encrypted_message[index:]
    elif action == "ChangeAll":
        char_to_replace = instruction[1]
        new_char = instruction[2]
        encrypted_message = encrypted_message.replace(char_to_replace, new_char)

print(f"The decrypted message is: {encrypted_message}")
