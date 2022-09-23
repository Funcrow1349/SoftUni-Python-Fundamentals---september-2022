nr_of_snowballs = int(input())
best_snowball = 0
weight_of_snowball = 0
speed_of_snowball = 0
quality_of_snowball = 0


for i in range(1, nr_of_snowballs + 1):
    snowball_weight = int(input())
    snowball_speed = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_weight / snowball_speed) ** snowball_quality)
    if snowball_value > best_snowball:
        best_snowball = snowball_value
        weight_of_snowball = snowball_weight
        speed_of_snowball = snowball_speed
        quality_of_snowball = snowball_quality

print(f"{weight_of_snowball} : {speed_of_snowball} = {best_snowball} ({quality_of_snowball})")
