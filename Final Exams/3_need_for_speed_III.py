number_of_cars = int(input())
cars_collection = {}
for entry in range(number_of_cars):
    current_entry = input().split("|")
    car = current_entry[0]
    mileage = int(current_entry[1])
    fuel = int(current_entry[2])
    if car not in cars_collection:
        cars_collection[car] = {}
    cars_collection[car]["Mileage"] = mileage
    cars_collection[car]["Fuel"] = fuel

while True:
    command = input()
    if command == "Stop":
        break
    instructions = command.split(" : ")
    action = instructions[0]
    car = instructions[1]
    if action == "Drive":
        distance = int(instructions[2])
        fuel = int(instructions[3])
        if fuel > cars_collection[car]["Fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars_collection[car]["Mileage"] += distance
            cars_collection[car]["Fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_collection[car]["Mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del cars_collection[car]
    elif action == "Refuel":
        fuel = int(instructions[2])
        if fuel > 75 - cars_collection[car]["Fuel"]:
            refuel = 75 - cars_collection[car]["Fuel"]
            cars_collection[car]["Fuel"] = 75
            print(f"{car} refueled with {refuel} liters")
        else:
            cars_collection[car]["Fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        kilometres = int(instructions[2])
        if cars_collection[car]["Mileage"] - kilometres < 10000:
            cars_collection[car]["Mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometres} kilometers")
            cars_collection[car]["Mileage"] -= kilometres

for car in cars_collection.keys():
    print(f"{car} -> Mileage: {cars_collection[car]['Mileage']} kms, Fuel in the tank: {cars_collection[car]['Fuel']} lt.")

