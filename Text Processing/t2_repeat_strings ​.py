sequence = input().split()
for item in sequence:
    current_string = item * len(item)
    print(f"{current_string}", end="")