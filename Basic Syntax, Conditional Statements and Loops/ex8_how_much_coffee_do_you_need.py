current_command = input()
coffees = 0
while True:
    if current_command == "END":
        break
    elif current_command not in["cat", "CAT", "dog", "DOG", "coding", "CODING", "movie", "MOVIE"]:
        current_command = input()
        continue
    else:
        if current_command in ["coding", "cat", "dog", "movie"]:
            coffees += 1
        else:
            coffees += 2
        current_command = input()

if coffees > 5:
    print(f"You need extra sleep")
else:
    print(coffees)

