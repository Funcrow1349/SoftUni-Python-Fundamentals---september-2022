energy = int(input())
battles_won = 0
battle_ended = False

while True:
    command = input()
    if command == "End of battle":
        battle_ended = True
        break
    command = int(command)
    if command <= energy:
        battles_won += 1
        energy -= command
        if battles_won % 3 == 0:
            energy += battles_won
    else:
        break

if battle_ended:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")