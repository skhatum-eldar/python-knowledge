# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
# n = int(input('Enter the number of coins: '))
# eagle_count = 0
# tail_count = 0

# for i in range(n):
#     m = int(input('Enter if its eagle (0) or tail (1): '))
#     if m == 0:
#         eagle_count += 1
#     if m == 1:
#         tail_count +=1
# if eagle_count > tail_count:
#     print(f'YOU NEED TO TURN OVER {tail_count} TAILS')
# else:
#     print(f'YOU NEED TO TURN OVER {eagle_count} EAGLES')


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
# s = int(input('Enter the sum of 2 numbers: '))
# p = int(input('Enter the product of 2 numbers: '))

# for x in range(1, 1001):
#     for y in range(1, 1001):
#         if x + y == s and x * y == p:
#             print(f'x = {x}, y = {y}')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
# N = int(input('Enter the number: '))
# i = 1
# while i <= N:
#     print(i, end = ' ')
#     i = 2 * i