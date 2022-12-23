import random
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
# factorial = int(input('If you want to know \
# Factorial(N), pls input your integer number here: '))
# if factorial == 0:
#     print(factorial + 1)
# else:
#     count = 1
#     n = 1
#     while count < factorial+1:
#         n = n * count
#         count = count + 1
#         print (n)
#     print(f'{factorial}! = {n}')

# def factorial_finder (input_factorial):
#     if input_factorial == 0:
#         print ("All right megabrain your F(n):")
#         return input_factorial + 1
#     else:
#         count = 1
#         n = 1
#         while count < input_factorial+1:
#             n = n * count
#             count = count + 1
#             print (f'{count-1}! = {n}')
#         return n

# factorial = input('If you want to know \
# Factorial(N), pls input your integer number which is GREATER than ZERO  here: ')
# if factorial.isdigit()==True:
#     factorial = int(factorial)
#     print(f'So, you want to know {factorial}! and it\'s {factorial_finder(factorial)}')
# else:
#     print ("I was asking you to input INTEGER number MORE than zero, sorry, but you have to run the programe again")

# решение 2й. чуть более пайтоновское, но без проверок и методов
# простите за лень

# num = int(input ("input your integer number here: "))
# n = 1
# for dig in range (1, num+1):
#     n = n*dig
#     print (n)

#Задача 3. Задайте список из n чисел заполненый по формуле 
# (1+ 1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2,2,2,2,2,3] -> 13

# def make_my_list(user_num):
#     my_list = []
#     for num in range(1, user_num+1):
#         my_list.append(round((1+1/num)**num))
#     return my_list
    
# user_input = int(input('Pls, input integer and positive number that will be lenght of your list here: '))
# print (f"Your own list is {make_my_list(user_input)}, and the sum of the elements is '{sum(make_my_list(user_input))}'")

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах, получается). Позиции хранятся в файле file.txt 
# в одной строке одно число.

def make_my_list(user_num):
    my_list = []
    for num in range(-user_num, user_num+1):
        my_list.append(num)
    return my_list

with open ('file.txt', 'w') as data:
    data.write ('1\n')
    data.write ('3\n')
    
my_file = open('file.txt','r')
first_pos = int(my_file.readline())
second_pos = int(my_file.readline(2))
my_file.close

user_input = input('Input integer number, whatever you want, here: ')
if user_input.isdigit()==True:
    user_input = int(user_input)
    new_list = make_my_list (user_input)
else:
    print ("I was asking you to input INTEGER number, sorry, but you have to run the programe again")
mult_pos = (new_list[first_pos-1])*(new_list[second_pos-1])

print (f'your list is {new_list}\nAnd the product of numbers on "{first_pos}" and "{second_pos}" positions is "{mult_pos}"')

# Задача 5. Реализуйте алгоритм перемешивания списка без шафл
#список я взял из задачи 4


for num in range(len(new_list)):
    i = random.randint(0, len(new_list)-1)
    new_list[i], new_list[num] = new_list[num], new_list[i]

print (f'This is new shuffled list {new_list}')
