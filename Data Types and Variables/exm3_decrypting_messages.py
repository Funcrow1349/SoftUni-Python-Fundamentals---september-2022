key = int(input())
nr_of_lines = int(input())
decrypted_phrase = ""

for symbol in range(nr_of_lines):
    current_symbol = ord(input())
    decrypted_phrase += chr(current_symbol + key)

print(decrypted_phrase)