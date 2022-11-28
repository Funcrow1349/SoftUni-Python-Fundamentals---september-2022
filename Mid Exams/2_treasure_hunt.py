treasure_chest = input().split("|")
total_gain = 0

while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    elif command[0] == "Loot":
        for i in range(len(command)):
            if i == 0:
                continue
            item = command[i]
            if item not in treasure_chest:
                treasure_chest.insert(0, item)
    elif command[0] == "Drop":
        position = int(command[1])
        if 0 <= position < len(treasure_chest):
            current_loot = treasure_chest.pop(position)
            treasure_chest.append(current_loot)
        else:
            continue
    elif command[0] == "Steal":
        count = int(command[1])
        if count >= len(treasure_chest):
            removed = treasure_chest
            print(', '.join(removed))
            print('Failed treasure hunt.')
            exit()
        else:
            removed = treasure_chest[-count:]
            del treasure_chest[-count:]
            print(', '.join(removed))

if len(treasure_chest) > 0:
    for i in range(len(treasure_chest)):
        total_gain += len(treasure_chest[i])
    average_gain = f"{total_gain / len(treasure_chest):.2f}"
    print(f"Average treasure gain: {average_gain} pirate credits.")





