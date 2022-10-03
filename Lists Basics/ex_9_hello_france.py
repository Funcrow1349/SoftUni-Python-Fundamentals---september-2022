collection_of_items = input().split("|")
budget = float(input())
bought_items = []
total_profit = 0

for item in collection_of_items:
    current_item = item.split("->")
    if current_item[0] == "Clothes" and float(current_item[1]) <= 50 and float(current_item[1]) <= budget:
        budget -= float(current_item[1])
        bought_items.append(item)
    elif current_item[0] == "Shoes" and float(current_item[1]) <= 35 and float(current_item[1]) <= budget:
        budget -= float(current_item[1])
        bought_items.append(item)
    elif current_item[0] == "Accessories" and float(current_item[1]) <= 20.5 and float(current_item[1]) <= budget:
        budget -= float(current_item[1])
        bought_items.append(item)
for element in bought_items:
    current_element = element.split("->")
    current_profit = float(current_element[1]) * 1.40
    total_profit += current_profit - float(current_element[1])
    budget += current_profit
    print(f"{current_profit:.2f}", end=" ")

print(f"\nProfit: {total_profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
