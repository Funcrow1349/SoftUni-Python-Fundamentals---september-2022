fire_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
print("Cells: ")

for fire in fire_cells:
    fire_type = fire.split(" = ")
    if fire_type[0] == "High" and 80 < int(fire_type[1]) <= 125:
        if int(fire_type[1]) <= water:
            total_fire += int(fire_type[1])
            water -= int(fire_type[1])
            effort += int(fire_type[1]) * 0.25
            print(f" - {int(fire_type[1])}")
    elif fire_type[0] == "Medium" and 50 < int(fire_type[1]) <= 80:
        if int(fire_type[1]) <= water:
            total_fire += int(fire_type[1])
            water -= int(fire_type[1])
            effort += int(fire_type[1]) * 0.25
            print(f" - {int(fire_type[1])}")
    elif fire_type[0] == "Low" and 0 < int(fire_type[1]) <= 50:
        if int(fire_type[1]) <= water:
            total_fire += int(fire_type[1])
            water -= int(fire_type[1])
            effort += int(fire_type[1]) * 0.25
            print(f" - {int(fire_type[1])}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")