products = {}
while True:
    current_command = input()
    if current_command == "buy":
        break
    current_order = current_command.split()
    product = current_order[0]
    price = float(current_order[1])
    quantity = int(current_order[2])
    if product not in products.keys():
        products[product] = []
        products[product].append(price)
        products[product].append(quantity)
    else:
        if products[product][0] != price:
            products[product][0] = price
        products[product][1] += quantity

for key, value in products.items():
    price_of_item = value[0] * value[1]
    print(f"{key} -> {price_of_item:.2f}")
