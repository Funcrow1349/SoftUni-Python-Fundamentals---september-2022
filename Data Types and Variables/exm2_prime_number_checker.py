number = int(input())
is_prime = True
for current_number in range(2, number):
    if number % current_number == 0:
        is_prime = False

print(is_prime)