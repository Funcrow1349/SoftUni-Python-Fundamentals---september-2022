houses = [int(num) for num in input().split("@")]
cupid_position = 0
while True:
    command = input()
    if command == "Love!":
        break
    current_command = command.split()
    jump_length = int(current_command[1])
    target_jump = cupid_position + jump_length
    if target_jump >= len(houses):
        target_jump = 0
    cupid_position = target_jump
    if houses[target_jump] == 0:
        print(f"Place {target_jump} already had Valentine's day.")
    elif houses[target_jump] > 0:
        houses[target_jump] -= 2
        if houses[target_jump] == 0:
            print(f"Place {target_jump} has Valentine's day.")

failed_houses = 0
for house in range(len(houses)):
    if houses[house] != 0:
        failed_houses += 1

print(f"Cupid's last position was {cupid_position}.")
if failed_houses != 0:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")
