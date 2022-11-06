parking_lot = {}
number_of_entries = int(input())
for entry in range(number_of_entries):
    command = input().split()
    action = command[0]
    username = command[1]
    if action == "register":
        car_plate = command[2]
        if username not in parking_lot.keys():
            parking_lot[username] = car_plate
            print(f"{username} registered {car_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {car_plate}")
    elif action == "unregister":
        if username not in parking_lot.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking_lot[username]
            print(f"{username} unregistered successfully")

for username, car_plate in parking_lot.items():
    print(f"{username} => {car_plate}")
