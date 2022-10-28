shelf_with_books = input().split("&")
while True:
    command = input()
    if command == "Done":
        break
    if "Add Book" in command:
        current_command = command.split(" | ")
        current_book = current_command[1]
        if current_book not in shelf_with_books:
            shelf_with_books.insert(0, current_book)
    elif "Take Book" in command:
        current_command = command.split(" | ")
        current_book = current_command[1]
        if current_book in shelf_with_books:
            shelf_with_books.remove(current_book)
    elif "Swap Books" in command:
        current_command = command.split(" | ")
        first_book = current_command[1]
        second_book = current_command[2]
        if first_book in shelf_with_books and second_book in shelf_with_books:
            index_of_first_book = shelf_with_books.index(first_book)
            index_of_second_book = shelf_with_books.index(second_book)
            shelf_with_books[index_of_first_book], shelf_with_books[index_of_second_book] = \
                shelf_with_books[index_of_second_book], shelf_with_books[index_of_first_book]
    elif "Insert Book" in command:
        current_command = command.split(" | ")
        current_book = current_command[1]
        if current_book not in shelf_with_books:
            shelf_with_books.append(current_book)
    elif "Check Book" in command:
        current_command = command.split(" | ")
        index_of_book = int(current_command[1])
        if 0 <= index_of_book < len(shelf_with_books):
            print(shelf_with_books[index_of_book])
print(", ".join(shelf_with_books))

