settlements = {}
while True:
    command = input()
    if command == "Sail":
        break
    city_info = command.split("||")
    city_name, population, gold = city_info[0], int(city_info[1]), int(city_info[2])
    if city_name not in settlements.keys():
        settlements[city_name] = [0, 0]
    settlements[city_name][0] += population
    settlements[city_name][1] += gold

while True:
    command = input()
    if command == "End":
        break
    instructions = command.split("=>")
    action = instructions[0]
    if action == "Plunder":
        town, people, gold = instructions[1], int(instructions[2]), int(instructions[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        settlements[town][0] -= people
        settlements[town][1] -= gold
        if settlements[town][0] <= 0 or settlements[town][1] <= 0:
            del settlements[town]
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        town, gold = instructions[1], int(instructions[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            settlements[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {settlements[town][1]} gold.")

if settlements:
    print(f"Ahoy, Captain! There are {len(settlements)} wealthy settlements to go to:")
    for settlement, valuables in settlements.items():
        print(f"{settlement} -> Population: {valuables[0]} citizens, Gold: {valuables[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")