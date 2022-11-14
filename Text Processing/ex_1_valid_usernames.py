usernames = input().split(", ")
for username in usernames:
    is_valid = True
    if 3 <= len(username) <= 16:
        for char in username:
            if not (char.isalnum() or char == "-" or char == "_"):
                is_valid = False
            if char == " ":
                is_valid = False
    else:
        is_valid = False
    if is_valid:
        print(username)


