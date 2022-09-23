first_index = int(input())
last_index = int(input())


for a in range(first_index, last_index + 1):
    current_symbol = chr(a)
    print(current_symbol, end= " ")