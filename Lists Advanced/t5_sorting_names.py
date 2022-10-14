string_of_names = input().split(", ")
order_of_names = sorted(string_of_names, key=lambda name: (-len(name), name))
print(order_of_names)