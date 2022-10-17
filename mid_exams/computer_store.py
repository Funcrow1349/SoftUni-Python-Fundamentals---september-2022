price_without_taxes = 0
taxes = 0


while True:
    command = input()
    if command == "special" or command == "regular":
        break
    command = float(command)
    if command < 0:
        print("Invalid price!")
    else:
        price_without_taxes += command
        taxes += command * 0.20

total_price = price_without_taxes + taxes
if command == "special":
    total_price = total_price * 0.90

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")