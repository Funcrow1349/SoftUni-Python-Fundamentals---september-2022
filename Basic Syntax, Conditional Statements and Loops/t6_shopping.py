budget = int(input())

while True:
    product_price = input()
    if product_price != "End":
        product_price = int(product_price)
        if product_price > budget:
            print(f"You went in overdraft!")
            break
        budget -= product_price
    else:
        print("You bought everything needed.")
        break