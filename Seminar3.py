# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# # 1 решение
# list_1 = [1, 1, 2, 3, 0, -4, 4, 4]
# print(set(list_1))
# print(len(set(list_1)))

# 2 решение
# list_1 = [1, 1, 2, 2, 3, 3, 4, 4]
# result_list = list()
# for i in list_1:
#     if i not in result_list:
#         result_list.append(i)
# print(result_list)
# print(len(result_list))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.
# list_1 = [1, 2, 3, 4, 5]
# result_list = list()
# j = 0

# K = int(input('Enter the number: '))
# for i in list_1:
#     # if i < K - 1:
#     #     result_list[i] = list_1[K + 1]
#     # if i >= K:
#     #     result_list[i] = list_1[j]
#     #     j += 1
#     result_list[i] = list_1[-K]
#     K = K + 1
# print(result_list)
# print(list_1[-K])

# 1 вариант
# list_1 = [1, 2, 3, 4, 5]
# k = int(input())
# k = k % len(list_1)
# list_result = list()

# for i in range(k):
#     list_result.append(list_1[len(list_1) - k + i])

# for i in range(len(list_1) - k):
#     list_result.append(list_1[i])
# print(list_result)

# # 2 вариант
# lst = [1, 2, 3, 4, 5]
# k = 2

# for i in range(k):
#     lst.insert(0, lst.pop(-1))
# print(lst)

# Напишите программу для печати всех уникальных значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

S = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
