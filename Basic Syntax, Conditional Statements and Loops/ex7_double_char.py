command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    else:
        for char in command:
            print(2 * char, end="")
        print()
    command = input()
