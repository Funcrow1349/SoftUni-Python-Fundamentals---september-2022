def password_validator(some_input):
    list_of_errors = []
    if len(some_input) < 6 or len(some_input) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_input.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digits = 0
    for symbol in some_input:
        if symbol.isdigit():
            digits += 1
    if digits < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()
password_checked = password_validator(password)
if len(password_checked) == 0:
    print("Password is valid")
else:
    print('\n'.join(password_checked))
