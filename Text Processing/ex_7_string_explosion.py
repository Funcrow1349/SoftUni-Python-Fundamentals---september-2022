the_string = input()
new_string = []
explosion_strength = 0

for index in range(len(the_string)):
    if the_string[index] == ">":
        print(">", end="")
        explosion_strength += int(the_string[index + 1])
    else:
        if explosion_strength > 0:
            explosion_strength -= 1
        else:
            print(the_string[index], end="")