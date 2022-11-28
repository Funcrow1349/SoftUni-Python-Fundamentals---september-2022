synonyms = {}
count_of_synonyms = int(input())

for i in range (count_of_synonyms):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word, synonym in synonyms.items():
    key = word
    value = ", ".join(synonym)
    print(f"{word} - {value}")
