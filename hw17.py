# Задача 1. Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# def sum_of_digits(user_number):
#     sum_up = 0
#     for symbol in user_number:
#         if symbol.isdigit()==True:
#             symbol = int (symbol)
#             sum_up = sum_up+symbol
#         else:
#             None
#     return sum_up

# print ("This program can sum up every digit in your input number")
# user_input = input ('Please input your number: ')
# print(sum_of_digits(user_input))

# Задача 2 Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#путём долгого всматривания в задачу, мне пришло озарение! 
# этож факториал!))
# решение не очень пайтоновское
factorial = int(input('If you want to know \
Factorial(N), pls input your number here: '))
if factorial == 0:
    print(factorial + 1)
else:
    count = 1
    n = 1
    while count < factorial+1:
        n = n * count
        count = count + 1
        print (n)
    print(f'{factorial}! = {n}')
#решение чуть более пайтоновское
# num = int(input ("dd "))
# for dig in range (1, num+1):
#     dig *= dig
#     print (dig)