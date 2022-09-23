lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
times_shield_broken = 0
total_price = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        total_price += helmet_price
    if i % 3 == 0:
        total_price += sword_price
        if i % 2 == 0:
            total_price += shield_price
            times_shield_broken += 1
            if times_shield_broken % 2 == 0:
                total_price += armor_price

print(f"Gladiator expenses: {total_price:.2f} aureus")