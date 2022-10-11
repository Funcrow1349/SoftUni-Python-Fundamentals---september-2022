import sys

initial_input = input().split()
line_of_integers = []
for sym in initial_input:
    line_of_integers.append(int(sym))
current_command = input()
while current_command != "end":
    if "exchange" in current_command:
        current_command = current_command.split()
        index_ex = int(current_command[1])
        mutated_list = []
        invalid_index = False
        if index_ex >= len(line_of_integers) or index_ex < 0:
            invalid_index = True
        else:
            for a in range(index_ex + 1, len(line_of_integers)):
                mutated_list.append(line_of_integers[a])
            for b in range(0, index_ex + 1):
                mutated_list.append(line_of_integers[b])
        if invalid_index:
            print("Invalid index")
        else:
            line_of_integers = mutated_list
    elif "max" in current_command and "odd" in current_command:
        max_odd_number = -sys.maxsize
        index_max_odd_number = 0
        max_odd_matches = False
        for num in line_of_integers:
            if num % 2 != 0 and num >= max_odd_number:
                max_odd_number = num
                index_max_odd_number = line_of_integers.index(num)
                max_odd_matches = True
        if not max_odd_matches:
            print("No matches")
        else:
            print(index_max_odd_number)
    elif "max" in current_command and "even" in current_command:
        max_even_number = -sys.maxsize
        index_max_even_number = 0
        max_even_matches = False
        for num in line_of_integers:
            if num % 2 == 0 and num >= max_even_number:
                max_even_number = num
                index_max_even_number = line_of_integers.index(num)
                max_even_matches = True
        if not max_even_matches:
            print("No matches")
        else:
            print(index_max_even_number)
    elif "min" in current_command and "odd" in current_command:
        min_odd_number = sys.maxsize
        index_min_odd_number = 0
        min_odd_matches = False
        for num in line_of_integers:
            if num % 2 != 0 and num <= min_odd_number:
                min_odd_number = num
                index_min_odd_number = line_of_integers.index(num)
                min_odd_matches = True
        if not min_odd_matches:
            print("No matches")
        else:
            print(index_min_odd_number)
    elif "min" in current_command and "even" in current_command:
        min_even_number = sys.maxsize
        index_min_even_number = 0
        min_even_matches = False
        for num in line_of_integers:
            if num % 2 == 0 and num <= min_even_number:
                min_even_number = num
                index_min_even_number = line_of_integers.index(num)
                min_even_matches = True
        if not min_even_matches:
            print("No matches")
        else:
            print(index_min_even_number)
    elif "first" in current_command and "odd" in current_command:
        current_command = current_command.split()
        first_odd_count = int(current_command[1])
        first_odd_list = []
        invalid_count = False
        for num in line_of_integers:
            if first_odd_count > len(line_of_integers):
                invalid_count = True
                break
            if num % 2 != 0:
                first_odd_list.append(num)
                if len(first_odd_list) == first_odd_count:
                    break
        if invalid_count:
            print("Invalid count")
        else:
            print(first_odd_list)
    elif "first" in current_command and "even" in current_command:
        current_command = current_command.split()
        first_even_count = int(current_command[1])
        first_even_list = []
        invalid_count = False
        for num in line_of_integers:
            if first_even_count > len(line_of_integers):
                invalid_count = True
                break
            if num % 2 == 0:
                first_even_list.append(num)
                if len(first_even_list) == first_even_count:
                    break
        if invalid_count:
            print("Invalid count")
        else:
            print(first_even_list)
    elif "last" in current_command and "odd" in current_command:
        current_command = current_command.split()
        last_odd_count = int(current_command[1])
        last_odd_list_reversed = []
        invalid_count = False
        for num in range(len(line_of_integers) - 1, -1, -1):
            if last_odd_count > len(line_of_integers):
                invalid_count = True
                break
            if line_of_integers[num] % 2 != 0:
                last_odd_list_reversed.append(line_of_integers[num])
                if len(last_odd_list_reversed) == last_odd_count:
                    break
        if invalid_count:
            print("Invalid count")
        else:
            if len(last_odd_list_reversed) >= 1:
                print(last_odd_list_reversed)
            else:
                last_odd_list_reversed.reverse()
                print(last_odd_list_reversed)
    elif "last" in current_command and "even" in current_command:
        current_command = current_command.split()
        last_even_count = int(current_command[1])
        last_even_list_reversed = []
        invalid_count = False
        for num in range(len(line_of_integers) - 1, -1, -1):
            if last_even_count > len(line_of_integers):
                invalid_count = True
                break
            if line_of_integers[num] % 2 == 0:
                last_even_list_reversed.append(line_of_integers[num])
                if len(last_even_list_reversed) == last_even_count:
                    break
        if invalid_count:
            print("Invalid count")
        else:
            if len(last_even_list_reversed) >= 1:
                print(last_even_list_reversed)
            else:
                last_even_list_reversed.reverse()
                print(last_even_list_reversed)
    current_command = input()
print(line_of_integers)