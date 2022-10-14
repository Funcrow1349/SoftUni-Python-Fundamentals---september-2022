nr_of_wagons = int(input())
wagons = [0] * nr_of_wagons
current_command = input().split()

while "End" not in current_command:
    if current_command[0] == "add":
        wagons[-1] += int(current_command[1])
    elif current_command[0] == "insert":
        wagons[int(current_command[1])] += int(current_command[2])
    elif current_command[0] == "leave":
        wagons[int(current_command[1])] -= int(current_command[2])
    current_command = input().split()
print(wagons)
