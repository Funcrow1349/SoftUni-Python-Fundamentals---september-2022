entry = input()
phonebook = {}

while "-" in entry:
    current_entry = entry.split("-")
    name = current_entry[0]
    number = current_entry[1]
    phonebook[name] = number
    entry = input()

search_count = int(entry)
for item in range(search_count):
    request = input()
    if request not in phonebook.keys():
        print(f"Contact {request} does not exist.")
    else:
        print(f"{request} -> {phonebook[request]}")
