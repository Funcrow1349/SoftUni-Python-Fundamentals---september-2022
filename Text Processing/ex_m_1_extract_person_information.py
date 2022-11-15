nr_of_entries = int(input())
for entry in range(nr_of_entries):
    current_entry = input()
    name = ""
    age = ""
    for index in range(len(current_entry)):
        if current_entry[index] == "@":
            for ind in range(index + 1, len(current_entry)):
                if current_entry[ind] == "|":
                    break
                else:
                    name += current_entry[ind]
        elif current_entry[index] == "#":
            for ind in range(index + 1, len(current_entry)):
                if current_entry[ind] == "*":
                    break
                else:
                    age += current_entry[ind]
    print(f"{name} is {int(age)} years old.")