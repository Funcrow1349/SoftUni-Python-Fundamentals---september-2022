text = input()
text = text.lower()

my_list = ["sand", "water", "fish", "sun"]
counter = 0

for item in my_list:
    if item in text:
        word_count_txt = text.count(item)
        counter += word_count_txt

print(counter)