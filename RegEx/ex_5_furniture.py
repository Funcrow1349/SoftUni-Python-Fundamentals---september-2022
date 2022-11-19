import re

pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)"
bought_furniture = []
total_sum = 0

while True:
    command = input()
    if command == "Purchase":
        break
    matches = re.search(pattern, command)
    if matches:
        furniture, price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_sum += float(price) * int(quantity)

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_sum:.2f}")
