current_product = input()
current_quantity = int(input())


def price_calc(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "water":
        return quantity * 1.00
    elif product == "coke":
        return quantity * 1.40
    elif product == "snacks":
        return quantity * 2.00


print(f"{price_calc(current_product, current_quantity):.2f}")