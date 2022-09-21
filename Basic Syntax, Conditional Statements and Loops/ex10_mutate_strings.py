word_1 = input()
word_2 = input()
word_final = ""
prev_word = ""
n = 1

for i in range(len(word_1)):
    word_final += word_2[:n] + word_1[n:]
    n += 1
    if word_final != word_1 and word_final != prev_word:
        print(word_final)
        prev_word = word_final
        word_final = ""
    else:
        word_final = ""
        continue
