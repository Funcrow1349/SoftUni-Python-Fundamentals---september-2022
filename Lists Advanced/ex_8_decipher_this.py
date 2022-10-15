def decipher_message(some_message):
    deciphered_message = []
    for word in some_message:
        key_digit = []
        word = list(word)
        for char in word:
            if char.isdigit():
                key_digit.append(char)
        ascii_number = "".join(key_digit)
        symbol = chr(int(ascii_number))
        word.insert(0, symbol)
        for item in range(len(word) -1, -1, -1):
            if word[item].isdigit():
                word.remove(word[item])
        word[1], word[-1] = word[-1], word[1]
        deciphered_message.append("".join(word))
    return " ".join(deciphered_message)


secret_message = input().split()
print(decipher_message(secret_message))