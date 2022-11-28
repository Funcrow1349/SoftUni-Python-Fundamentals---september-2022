import re
text = input()
total_calories = 0

search_pattern = r"(#|\|)([a-zA-Z\s?]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
food_supplies = re.findall(search_pattern, text)
for match in food_supplies:
    total_calories += int(match[3])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for match in food_supplies:
    food = match[1]
    exp_date = match[2]
    calories = int(match[3])
    print(f"Item: {food}, Best before: {exp_date}, Nutrition: {calories}")


