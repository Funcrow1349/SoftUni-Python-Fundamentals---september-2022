import sys

list_received = input().split()
list_of_integers = []
for char in list_received:
    list_of_integers.append(int(char))
numbers_to_remove = int(input())
for num in range(numbers_to_remove):
    current_smallest_number = sys.maxsize
    for char in list_of_integers:
        if char < current_smallest_number:
            current_smallest_number = char
    list_of_integers.remove(current_smallest_number)
string_of_integers = []
for integer in list_of_integers:
    string_of_integers.append(str(integer))
print(", ".join(string_of_integers))
