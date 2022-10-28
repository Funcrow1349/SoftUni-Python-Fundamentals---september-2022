travel_route = input().split("||")
starting_fuel = int(input())
starting_ammo = int(input())

for command in travel_route:
    if "Travel" in command:
        current_command = command.split()
        light_years = int(current_command[1])
        if starting_fuel >= light_years:
            print(f"The spaceship travelled {light_years} light-years.")
            starting_fuel -= light_years
        else:
            print("Mission failed.")
            break
    elif "Enemy" in command:
        current_command = command.split()
        enemy_armour = int(current_command[1])
        if starting_ammo >= enemy_armour:
            print(f"An enemy with {enemy_armour} armour is defeated.")
            starting_ammo -= enemy_armour
        elif starting_ammo < enemy_armour:
            if starting_fuel >= enemy_armour * 2:
                print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
                starting_fuel -= enemy_armour * 2
            else:
                print("Mission failed.")
                break
    elif "Repair" in command:
        current_command = command.split()
        fuel = int(current_command[1])
        ammo = fuel * 2
        starting_fuel += fuel
        starting_ammo += ammo
        print(f"Ammunitions added: {ammo}.")
        print(f"Fuel added: {fuel}.")
    elif "Titan" in command:
        print("You have reached Titan, all passengers are safe.")
        break


