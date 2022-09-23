nr_of_small_latin_letters = int(input())

for i in range(nr_of_small_latin_letters):
    for k in range(nr_of_small_latin_letters):
        for j in range(nr_of_small_latin_letters):
            print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")