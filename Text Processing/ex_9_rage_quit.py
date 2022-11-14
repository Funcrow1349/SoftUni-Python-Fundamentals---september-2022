sequence = input().upper()
temporary_message = []
final_message = []
unique_symbols = []
repeater = ""

for index in range(len(sequence)):
    if not sequence[index].isdigit():
        if sequence[index] not in unique_symbols:
            unique_symbols.append(sequence[index])
        temporary_message.append(sequence[index])
    else:
        repeater += sequence[index]
        if index < len(sequence) - 1:
            if sequence[index + 1].isdigit():
                repeater += sequence[index + 1]
        final_message.append(("".join(temporary_message)) * int(repeater))
        repeater = ""
        temporary_message.clear()

print(f"Unique symbols used: {len(unique_symbols)}")
print("".join(final_message))