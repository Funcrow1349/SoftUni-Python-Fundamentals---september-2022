areas_with_animals = {}
while True:
    command = input()
    if command == "EndDay":
        break
    instructions = command.split(": ")
    action = instructions[0]
    if action == "Add":
        tokens = instructions[1].split("-")
        animal_name, needed_food, area = tokens[0], int(tokens[1]), tokens[2]
        if area not in areas_with_animals.keys():
            areas_with_animals[area] = {}
        if animal_name not in areas_with_animals[area]:
            areas_with_animals[area][animal_name] = needed_food
        else:
            areas_with_animals[area][animal_name] += needed_food

    elif action == "Feed":
        tokens = instructions[1].split("-")
        animal_name, food_given = tokens[0], int(tokens[1])
        for area, animals in areas_with_animals.items():
            if animal_name in animals.keys():
                areas_with_animals[area][animal_name] -= food_given
                if areas_with_animals[area][animal_name] <= 0:
                    print(f"{animal_name} was successfully fed")
                    del areas_with_animals[area][animal_name]

print("Animals:")
for key, value in areas_with_animals.items():
    for animal in value.keys():
        print(f"{animal} -> {areas_with_animals[key][animal]}g")
print("Areas with hungry animals:")
for area, animals in areas_with_animals.items():
    hungry_animals = len(animals)
    if hungry_animals > 0:
        print(f"{area}: {hungry_animals}")