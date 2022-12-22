# Задача 1. Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

a = input ('dd: ')
sum = 0
for symbol in a:
    if symbol.isdigit()==True:
        symbol = int (symbol)
        sum = sum+symbol
    else:
        None
print(sum)