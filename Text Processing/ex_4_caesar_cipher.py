message_to_encrypt = input()
final_message = ""

for char in message_to_encrypt:
    final_message += chr(ord(char) + 3)
print(final_message)