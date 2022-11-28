resources = {}
nr_of_commands = 0
last_key = ""
while True:
    command = input()
    if command == "stop":
        break
    nr_of_commands += 1
    if nr_of_commands % 2 != 0:
        if command not in resources.keys():
            resources[command] = 0
        last_key = command
    else:
        resources[last_key] += int(command)

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")







