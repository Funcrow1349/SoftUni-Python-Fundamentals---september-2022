number_of_messages = int(input())

for i in range(number_of_messages):
    current_message = int(input())
    if current_message == 88:
        print("Hello")
    elif current_message == 86:
        print("How are you?")
    elif current_message < 88:
        print("GREAT!")
    else:
        print("Bye.")