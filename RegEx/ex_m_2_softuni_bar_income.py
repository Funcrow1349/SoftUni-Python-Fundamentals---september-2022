import re

global_pattern = r"\%([A-Z][a-z]+)\%[^\|\$\%\.]*?\<(\w+)\>[^\|\$\%\.]*?\|([0-9]+)\|[\w\-]*?([0-9.]+[0-9])(?=\$)"
total_income = 0

while True:
    command = input()
    if command == "end of shift":
        break
    matches = re.search(global_pattern, command)
    if matches:
        customer, product, count, price = matches.groups()
        print(f"{customer}: {product} - {(int(count) * float(price)):.2f}")
        total_income += int(count) * float(price)

print(f"Total income: {total_income:.2f}")