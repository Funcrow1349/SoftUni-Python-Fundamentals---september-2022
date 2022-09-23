nr_of_lines = int(input())
tank_capacity = 255

for i in range(nr_of_lines):
    litres = int(input())
    if tank_capacity < litres:
        print("Insufficient capacity!")
        continue
    else:
        tank_capacity -= litres

print(255 - tank_capacity)