number_of_lines = int(input())
balanced = True
previous_bracket = ""

for symbol in range(number_of_lines):
    current_symbol = input()
    if current_symbol == "(" or current_symbol == ")":
        if current_symbol != previous_bracket:
            previous_bracket = current_symbol
            if symbol == 0:
                if current_symbol == ")":
                    balanced = False
                    break
        else:
            balanced = False
            break
if previous_bracket == "(":
    balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")


