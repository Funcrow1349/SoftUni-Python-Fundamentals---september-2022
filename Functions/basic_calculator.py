# basic calculator
def intro():
    return '''##################################
# Welcome to SoftUni Calculator  #
#   Please select an option to   #
#          continue              #
#                                #
#                                #
#   Author: Ivaylo Ivanov        #
#   Course: SoftUni Fundamentals #
#                                #
##################################\n'''


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(intro())

while True:
    choice = input('1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\nEnter your choice: ')

    if choice == '5':
        print('Thank you for using our calculator!!!')
        break

    if choice == '1':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print('The result is: ', add(n1, n2), '\n')

    elif choice == '2':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print('The result is: ', subtract(n1, n2), '\n')

    elif choice == '3':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print('The result is: ', multiply(n1, n2), '\n')

    elif choice == '4':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print('The result is: ', divide(n1, n2), '\n')

    else:
        print('Wrong choice!!!\n')