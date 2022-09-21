n_times = int(input())

for i in range(n_times):
    text = input()
    pure = True
    for l in text:
        if l == "," or l == "." or l == "_":
            pure = False
            break
    if pure:
        print(f"{text} is pure.")
    else:
        print(f"{text} is not pure!")


