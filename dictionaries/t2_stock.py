initial_list = input().split()
command = input().split()
stock = {}

for index in range(0, len(initial_list), 2):
    key = initial_list[index]
    value = initial_list[index + 1]
    stock[key] = value

for current_command in command:
    if current_command in stock.keys():
        print(f"We have {stock[current_command]} of {current_command} left")
    else:
        print(f"Sorry, we don't have {current_command}")

