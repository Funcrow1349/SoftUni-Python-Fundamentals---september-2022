number_of_dragons = int(input())
dragons = {}
for dragon in range(number_of_dragons):
    current_dragon = input().split()
    dragon_type = current_dragon[0]
    dragon_name = current_dragon[1]
    if current_dragon[2] == "null":
        dragon_damage = 45
    else:
        dragon_damage = int(current_dragon[2])
    if current_dragon[3] == "null":
        dragon_health = 250
    else:
        dragon_health = int(current_dragon[3])
    if current_dragon[4] == "null":
        dragon_armor = 10
    else:
        dragon_armor = int(current_dragon[4])
    if dragon_type not in dragons.keys():
        dragons[dragon_type] = {}
    dragons[dragon_type][dragon_name] = [dragon_damage, dragon_health, dragon_armor]
average_stats = {}
for colour, names in dragons.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    for name, stats in names.items():
        total_damage += stats[0]
        total_health += stats[1]
        total_armor += stats[2]
    average_damage = total_damage / len(names)
    average_health = total_health / len(names)
    average_armor = total_armor / len(names)
    average_stats[colour] = [average_damage, average_health, average_armor]
for dragon_type, dragon_names in dragons.items():
    dragons[dragon_type] = {k: v for k, v in sorted(dragon_names.items(), key=lambda item: item[0])}
for dragon_type, dragon_stats in average_stats.items():
    print(f"{dragon_type}::({average_stats[dragon_type][0]:.2f}/{average_stats[dragon_type][1]:.2f}/{average_stats[dragon_type][2]:.2f})")
    for dragon_types, dragon_names in dragons.items():
        if dragon_types == dragon_type:
            for dragon_name, dr_stats in dragon_names.items():
                print(f"-{dragon_name} -> damage: {dr_stats[0]}, health: {dr_stats[1]}, armor: {dr_stats[2]}")