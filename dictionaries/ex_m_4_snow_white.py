dwarves = {}
while True:
    command = input()
    if command == "Once upon a time":
        break
    current_entry = command.split(" <:> ")
    current_dwarf = current_entry[0]
    current_hat_color = current_entry[1]
    current_physics = int(current_entry[2])
    if current_hat_color not in dwarves.keys():
        dwarves[current_hat_color] = {}
        if current_dwarf not in dwarves[current_hat_color].keys():
            dwarves[current_hat_color][current_dwarf] = current_physics
        else:
            if current_physics > dwarves[current_hat_color][current_dwarf]:
                dwarves[current_hat_color][current_dwarf] = current_physics
    else:
        if current_dwarf not in dwarves[current_hat_color].keys():
            dwarves[current_hat_color][current_dwarf] = current_physics
        else:
            if current_physics > dwarves[current_hat_color][current_dwarf]:
                dwarves[current_hat_color][current_dwarf] = current_physics
dwarfs_dict = {}
for hat_color, members in dwarves.items():
    hat_length = len(members)
    for dwarf, physics in members.items():
        dwarf_name_color = f"{dwarf}|{hat_color}"
        dwarfs_dict[dwarf_name_color] = {"name": dwarf, "physics": physics, "members": hat_length,
                                         "hat_color": hat_color}

for item in sorted(dwarfs_dict, key=lambda k: (dwarfs_dict[k]['physics'], dwarfs_dict[k]['members']), reverse=True):
    current_dwarf = dwarfs_dict[item]
    print(f"({current_dwarf['hat_color']}) {current_dwarf['name']} <-> {current_dwarf['physics']}")





