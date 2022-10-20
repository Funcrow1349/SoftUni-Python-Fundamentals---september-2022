def blacksmith_shop(some_journal):
    while True:
        command = input()
        if command == "Craft!":
            break
        current_command = command.split(" - ")
        action = current_command[0]
        item = current_command[1]
        if action == "Collect":
            if item not in some_journal:
                some_journal.append(item)
        elif action == "Drop":
            if item in some_journal:
                some_journal.remove(item)
        elif action == "Combine Items":
            items = item.split(":")
            first_item = items[0]
            second_item = items[1]
            if first_item in some_journal:
                index_of_first_item = some_journal.index(first_item)
                some_journal.insert(index_of_first_item + 1, second_item)
        elif action == "Renew":
            if item in some_journal:
                some_journal.remove(item)
                some_journal.append(item)
    return ", ".join(some_journal)


journal_of_items = input().split(", ")
print(blacksmith_shop(journal_of_items))
