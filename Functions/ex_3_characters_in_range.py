def string_chars(one, two):
    ascii_list = []
    for char in range(ord(one) + 1, ord(two)):
        ascii_list.append(chr(char))
    return ascii_list


char_one = input()
char_two = input()
print(" ".join(string_chars(char_one, char_two)))