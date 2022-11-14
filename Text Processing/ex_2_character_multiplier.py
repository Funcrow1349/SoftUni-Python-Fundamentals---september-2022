two_strings = input().split()
first_string = two_strings[0]
second_string = two_strings[1]
total_sum = 0

if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
else:
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
print(total_sum)

