part_to_cut = input()
expression = input()

while part_to_cut in expression:
    expression = expression.replace(part_to_cut, "")

print(expression)