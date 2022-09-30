number_of_lines = int(input())
word = input()
first_list = []

for entry in range(number_of_lines):
    current_entry = input()
    first_list.append(current_entry)
print(first_list)

for i in range(len(first_list) -1, -1, -1):
    element = first_list[i]
    if word not in element:
        first_list.remove(element)

print(first_list)