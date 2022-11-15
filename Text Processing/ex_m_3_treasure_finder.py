key = input().split()
decrypted_messages = []
while True:
    command = input()
    if command == "find":
        break
    decrypted_message = ""
    index = 0
    for char in command:
        while True:
            decrypted_message += chr(ord(char) - int(key[index]))
            if index == len(key) - 1:
                index = 0
            else:
                index += 1
            break
    decrypted_messages.append(decrypted_message)

for message in decrypted_messages:
    type_of_treasure = ""
    coordinates = ""
    for index in range(len(message)):
        treasure_found = False
        if message[index] == "&":
            for ind in range(index + 1, len(message)):
                if message[ind] == "&":
                    treasure_found = True
                    break
                else:
                    type_of_treasure += message[ind]
        if treasure_found:
            break
    for index in range(len(message)):
        treasure_found = False
        if message[index] == "<":
            for ind in range(index + 1, len(message)):
                if message[ind] == ">":
                    treasure_found = True
                    break
                else:
                    coordinates += message[ind]
        if treasure_found:
            break
    print(f"Found {type_of_treasure} at {coordinates}")



