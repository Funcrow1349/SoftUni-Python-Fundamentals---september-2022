def analyze_command(command):
    if command == "int":
        number = int(input())
        return number * 2
    elif command == "real":
        number = float(input())
        result = number * 1.5
        return f"{result:.2f}"
    elif command == "string":
        word = input()
        return f"${word}$"


current_command = input()
print(analyze_command(current_command))