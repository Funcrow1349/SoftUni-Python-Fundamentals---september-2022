list_of_characters = input().split(", ")
my_dictionary = {key: ord(key) for key in list_of_characters}
print(my_dictionary)