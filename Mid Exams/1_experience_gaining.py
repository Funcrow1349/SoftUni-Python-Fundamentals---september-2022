exp_to_unlock_tank = float(input())
count_of_battles = int(input())
tank_unlocked = False
battles = 0
total_exp = 0

for battle in range(1, count_of_battles + 1):

    current_experience = float(input())
    battles += 1
    bonus_exp = 0
    if battle % 3 == 0:
        bonus_exp += (current_experience * 1.15) - current_experience
    if battle % 5 == 0:
        bonus_exp += (current_experience * 0.90) - current_experience
    if battle % 15 == 0:
        bonus_exp += (current_experience * 1.05) - current_experience
    total_exp += current_experience + bonus_exp
    if total_exp >= exp_to_unlock_tank:
        tank_unlocked = True
        break


diff = abs(exp_to_unlock_tank - total_exp)

if tank_unlocked:
    print(f"Player successfully collected his needed experience for {battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {diff:.2f} more needed.")



