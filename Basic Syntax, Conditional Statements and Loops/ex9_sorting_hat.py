name = input()
voldemort_name_spoken = False

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        voldemort_name_spoken = True
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()

if not voldemort_name_spoken:
    print("Welcome to Hogwarts.")
