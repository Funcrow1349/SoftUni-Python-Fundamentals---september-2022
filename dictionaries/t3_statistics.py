command = input()
my_dictionary = {}

while command != "statistics":
    pair = command.split(": ")
    key = pair[0]
    value = int(pair[1])
    if key not in my_dictionary:
        my_dictionary[key] = 0
    my_dictionary[key] += value
    command = input()

print("Products in stock:")

for product, quantity in my_dictionary.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(my_dictionary.keys())}")
print(f"Total Quantity: {sum(my_dictionary.values())}")

