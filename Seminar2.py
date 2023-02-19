# print(*range(5))
# print(list(range(5)))

# n = int(input('Enter the number: '))
# i = 1
# N = 1
# while i <= n:
#     N = N * i
#     i += 1
# print(f'Factorial {n} is {N}')

# n = int(input('Enter the number: '))
# a = 0
# b = 1
# c = 0
# i = 2
# while c < n:
#     c = a + b
#     a = b
#     b = c
#     i += 1
# if c == n:
#     print(f'YES! THE NUMBER {n} IS PART OF THE FIBONACCI WITH INDEX {i}!')
# else:
#     print('NOPE! -1')

# n = int(input('Enter the number of the days: '))
# i = 0
# count = 0
# res = 0
# while i < n:
#     m = int(input('Enter the temperature: '))
#     i += 1
#     if m > 0:
#         count += 1
#     else:
#         count = 0
#     if count > res:
#         res = count
# print(f'THE RESULT IS {res}')

n = int(input('Enter the number of watermelons: '))
max = 0
min = 1000

for i in range(n):
    m = int(input('Enter the weight: '))
    if m > max:
        max = m
    if m < min:
        min = m
print(f'MAX IS {max}, MIN IS {min}')


