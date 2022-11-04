list_of_elements = [element.lower() for element in input().split()]
my_dictionary = {}

for element in list_of_elements:
    if element not in my_dictionary.keys():
        my_dictionary[element] = []
    my_dictionary[element].append(element)

uneven_elements = []
for value in my_dictionary.values():
    if len(value) % 2 != 0:
        uneven_elements.append(value[0])

print(" ".join(uneven_elements))