quantity_of_decorations = int(input())
days_left_until_christmas = int(input())
total_cost = 0
christmas_spirit = 0

for current_day in range(1, days_left_until_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += quantity_of_decorations * 2
        christmas_spirit += 5
    if current_day % 3 == 0:
        total_cost += quantity_of_decorations * 5 + quantity_of_decorations * 3
        christmas_spirit += 13
    if current_day % 5 == 0:
        total_cost += quantity_of_decorations * 15
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        total_cost += 5 + 3 + 15
if days_left_until_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")


