string_of_sums = input().split(", ")
number_of_beggars = int(input())
list_of_sums = []

for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for i in range(current_beggar, len(string_of_sums), number_of_beggars):
        current_sum = int(string_of_sums[i])
        current_beggar_sum += current_sum
    list_of_sums.append(current_beggar_sum)
    current_beggar_sum -= current_beggar_sum

print(list_of_sums)




