number_of_heroes = int(input())
heroes = {}
for entry in range(number_of_heroes):
    current_entry = input().split(" ")
    hero_name = current_entry[0]
    hit_points = int(current_entry[1])
    mana_points = int(current_entry[2])
    heroes[hero_name] = {}
    heroes[hero_name]["HP"] = hit_points
    heroes[hero_name]["MP"] = mana_points

while True:
    command = input()
    if command == "End":
        break
    instructions = command.split(" - ")
    action = instructions[0]
    hero_name = instructions[1]
    if action == "CastSpell":
        mana_needed = int(instructions[2])
        spell_name = instructions[3]
        if mana_needed > heroes[hero_name]["MP"]:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            heroes[hero_name]["MP"] -= mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
    elif action == "TakeDamage":
        damage = int(instructions[2])
        attacker = instructions[3]
        if damage >= heroes[hero_name]["HP"]:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
        else:
            heroes[hero_name]["HP"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
    elif action == "Recharge":
        amount = int(instructions[2])
        if amount + heroes[hero_name]["MP"] > 200:
            amount -= (amount + heroes[hero_name]["MP"]) - 200
        heroes[hero_name]["MP"] += amount
        print(f"{hero_name} recharged for {amount} MP!")
    elif action == "Heal":
        amount = int(instructions[2])
        if amount + heroes[hero_name]["HP"] > 100:
            amount -= (amount + heroes[hero_name]["HP"]) - 100
        heroes[hero_name]["HP"] += amount
        print(f"{hero_name} healed for {amount} HP!")

for hero in heroes.keys():
    print(f"{hero}\n  HP: {heroes[hero]['HP']}\n  MP: {heroes[hero]['MP']}")
