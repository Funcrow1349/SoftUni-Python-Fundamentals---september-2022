message = input()
for index in range(len(message)):
    if message[index] == ":":
        print(f":{message[index + 1]}")


