number_of_lines = int(input())
plant_collection = {}
for entry in range(number_of_lines):
    current_plant = input().split("<->")
    plant_name = current_plant[0]
    plant_rarity = int(current_plant[1])
    plant_collection[plant_name] = {"Rarity": plant_rarity, "Rating": []}

while True:
    command = input()
    if command == "Exhibition":
        break
    instructions = command.split(": ")
    action = instructions[0]
    if action == "Rate":
        items = instructions[1].split(" - ")
        plant_to_rate = items[0]
        plant_rating = int(items[1])
        if plant_to_rate not in plant_collection.keys():
            print("error")
        else:
            plant_collection[plant_to_rate]["Rating"].append(plant_rating)
    elif action == "Update":
        items = instructions[1].split(" - ")
        plant_to_update = items[0]
        new_rarity = int(items[1])
        if plant_to_update not in plant_collection.keys():
            print("error")
        else:
            plant_collection[plant_to_update]["Rarity"] = new_rarity
    elif action == "Reset":
        plant_to_reset = instructions[1]
        if plant_to_reset not in plant_collection.keys():
            print("error")
        else:
            plant_collection[plant_to_reset]["Rating"] = []
print("Plants for the exhibition:")
for plant in plant_collection:
    if len(plant_collection[plant]['Rating']) == 0:
        print(f"- {plant}; Rarity: {plant_collection[plant]['Rarity']}; Rating: 0.00")
    else:
        print(f"- {plant}; Rarity: {plant_collection[plant]['Rarity']}; Rating: {sum(plant_collection[plant]['Rating']) / len(plant_collection[plant]['Rating']):.2f}")