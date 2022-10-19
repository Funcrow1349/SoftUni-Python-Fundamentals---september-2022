quantity_of_food = float(input()) * 1000
quantity_of_hay = float(input()) * 1000
quantity_of_cover = float(input()) * 1000
guinea_pigs_weight = float(input()) * 1000
food_not_enough = False

for day in range(1, 31):
    quantity_of_food -= 300
    if day % 2 == 0:
        quantity_of_hay -= quantity_of_food * 0.05
    if day % 3 == 0:
        quantity_of_cover -= guinea_pigs_weight / 3
    if quantity_of_food <= 0 or quantity_of_hay <= 0 or quantity_of_cover <= 0:
        food_not_enough = True

if food_not_enough:
    print("Merry must go to the pet store!")
else:
    food, hay, cover = quantity_of_food / 1000, quantity_of_hay / 1000, quantity_of_cover / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")


