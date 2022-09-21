budget = float(input())
flour_price = float(input())
egg_pack_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
bread_price = egg_pack_price + flour_price + milk_price
loaves_of_bread = 0
colored_eggs = 0

while budget >= bread_price:
    budget -= bread_price
    loaves_of_bread += 1
    colored_eggs += 3
    if loaves_of_bread % 3 == 0:
        colored_eggs -= loaves_of_bread - 2

print(f"You made {loaves_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
