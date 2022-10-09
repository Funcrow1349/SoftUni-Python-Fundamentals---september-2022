def loading_bar(some_number):
    if some_number == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"
    return f"{some_number}% [{'%' * (some_number // 10)}{'.' * (10 - some_number // 10)}]\nStill loading..."


decimal_number = int(input())
print(loading_bar(decimal_number))