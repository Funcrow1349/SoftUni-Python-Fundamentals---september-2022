password = input()

while True:
    command = input()
    if command == "Done":
        break
    instructions = command.split(" ")
    action = instructions[0]
    if action == "TakeOdd":
        new_password = ""
        for index in range(1, len(password), 2):
            new_password += password[index]
        password = new_password
        print(password)
    elif action == "Cut":
        index = int(instructions[1])
        length = int(instructions[2])
        substring = password[index: index + length]
        password = password.replace(substring, "", 1)
        print(password)
    elif action == "Substitute":
        substring = instructions[1]
        substitute = instructions[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
