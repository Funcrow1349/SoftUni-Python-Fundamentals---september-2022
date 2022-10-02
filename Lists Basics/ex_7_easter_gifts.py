list_of_gifts = input().split()
current_command = input().split()
while "Money" not in current_command:
    if "OutOfStock" in current_command:
        for element in range(len(list_of_gifts)):
            if current_command[1] in list_of_gifts[element]:
                list_of_gifts[element] = "None"
    elif "Required" in current_command:
        for element in range(len(list_of_gifts)):
            if element == int(current_command[2]):
                list_of_gifts[element] = current_command[1]
    elif "JustInCase" in current_command:
        list_of_gifts[-1] = current_command[1]
    current_command = input().split()

while "None" in list_of_gifts:
    list_of_gifts.remove("None")
for element in list_of_gifts:
    print(element, end=" ")
