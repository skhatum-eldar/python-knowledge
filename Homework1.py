# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
# a = int(input('Enter the 3 digit number: '))
# sum = 0
# while (a != 0):
#     sum += a % 10
#     a //= 10
# print(f'The sum is {sum}')


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
# s = int(input('Enter the total number of cranes: '))
# print(f'Petya and Seryoja did {s // 6} cranes, Katya did {s * 2 // 3} cranes')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
# ticket_number = int(input("Enter a 6-digit ticket number: "))
# first_3 = ticket_number // 1000
# sum1 = 0
# while first_3 > 0:
#     digit = first_3 % 10
#     sum1 += digit
#     first_3 //= 10

# last_3 = ticket_number % 1000
# sum2 = 0
# while last_3 > 0:
#     digit = last_3 % 10
#     sum2 += digit
#     last_3 //= 10

# if sum1 == sum2:
#     print('WOOHOO! YOUR TICKET IS VERY LUCKY!')
# else:
#     print('DONT BE SAD! EVEN IF THE TICKET IS UNLUCKY!')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input("Enter the number of rows of the chocolate bar: "))
m = int(input("Enter the number of columns of the chocolate bar: "))
k = int(input("Enter the number of pieces you want to break off: "))

total = n * m
if k <= total and (total - k) % 2 == 0:
    print(f'YES! ITS POSSIBLE TO BREAK OFF {k} PIECES!')
else:
    print(f'NOPE! ITS NOT POSSIBLE TO BREAK OFF {k} PIECES!')