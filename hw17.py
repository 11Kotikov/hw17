# Задача 1. Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_of_digits(user_number):
    sum_up = 0
    for symbol in user_number:
        if symbol.isdigit()==True:
            symbol = int (symbol)
            sum_up = sum_up+symbol
        else:
            None
    return sum_up

print ("This program can sum up every digit in your input number")
user_input = input ('Please input your number: ')
print(sum_of_digits(user_input))

