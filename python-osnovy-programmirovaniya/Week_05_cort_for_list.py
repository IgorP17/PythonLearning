# Даны два целых числа A и B (при этом A≤B).
# Выведите все числа от A до B включительно.
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     print(i, end=" ")

# Даны два целых числа A и В.
# Выведите все числа от A до B включительно, в порядке возрастания,если A < B,
# или в порядке убывания в противном случае.

# a = int(input())
# b = int(input())
#
# if a <= b:
#     for i in range(a, b + 1):
#         print(i, end=" ")
# else:
#     for i in range(a, b - 1, -1):
#         print(i, end=" ")

# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n флагов.
# Изображение одного флага имеет размер 4×4 символов, между двумя соседними флагами также имеется пустой
# (из пробелов) столбец. Разрешается вывести пустой столбец после последнего флага.
# Внутри каждого флага должен быть записан его номер — число от 1 до n.
# n = int(input())
# for i in range(1, n + 1):
#     print("+___", end=" ")
# print()
# for i in range(1, n + 1):
#     print("|" + str(i) + " /", sep="", end=" ")
# print()
# for i in range(1, n + 1):
#     print("|__\\", end=" ")
# print()
# for i in range(1, n + 1):
#     print("|   ", end=" ")

# По данному натуральному n≤9 выведите лесенку из n ступенек,
# i-я ступенька состоит из чисел от 1 до i без пробелов.
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

#
# numList = list(map(int, input().split()))
# print(', '.join(['Veni', 'Vidi', 'Vici']))
# inList = list(map(int, input().split()))

# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
# inList = list(input().split(" "))
# for i in range(len(inList)):
#     if i % 2 == 0:
#         print(inList[i], end=" ")

# Выведите все четные элементы списка.
# inList = list(map(int, input().split(" ")))
# for i in range(len(inList)):
#     if inList[i] % 2 == 0:
#         print(inList[i], end=" ")

# Найдите количество положительных элементов в данном списке.
# inList = list(map(int, input().split(" ")))
# cnt = 0
# for i in range(len(inList)):
#     if inList[i] > 0:
#         cnt += 1
# print(cnt)

# Найдите наибольшее значение в списке и индекс последнего элемента,
# который имеет данное значение за один проход по списку,
# не модифицируя этот список и не используя дополнительного списка
# inList = list(map(int, input().split()))
# mx = inList[0]
# idx = 0
# for i in range(len(inList)):
#     if inList[i] >= mx:
#         mx = inList[i]
#         idx = i
# print(mx, idx)

# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# 1 5 2 4 3
# 5 4
# inList = list(map(int, input().split()))
# prev = inList[0]
# for i in range(1, len(inList)):
#     if inList[i] > prev:
#         print(inList[i], end=" ")
#     prev = inList[i]

# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент,
# а значения всех элементов списка по модулю не превосходят 1000.
# inList = list(map(int, input().split()))
# mn = 1001
# for i in range(len(inList)):
#     if 0 < inList[i] < mn:
#         mn = inList[i]
# print(mn)

# print(' '.join(map(str, newList)))

# Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.
# len1 = int(input())
# inList = list(map(int, input().split()))
# x = int(input())
# delta = abs(x - inList[0])
# idx = 0
# for i in range(1, len(inList)):
#     if delta >= abs(x - inList[i]):
#         delta = abs(x - inList[i])
#         idx = i
# print(inList[idx])

# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.
# inList = list(map(int, input().split()))
# len1 = 0
# if len(inList) % 2 != 0:
#     len1 = len(inList) - 1
# else:
#     len1 = len(inList)
# for i in range(0, len1, 2):
#     inList[i], inList[i+1] = inList[i + 1], inList[i]
# print(' '.join(map(str, inList)))

# В списке все элементы попарно различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.
inList = list(map(int, input().split()))
mmin = mmax = inList[0]
min_idx = max_idx = 0
for i in range(len(inList)):
    if inList[i] >= mmax:
        mmax = inList[i]
        max_idx = i
    elif inList[i] <= mmin:
        mmin = inList[i]
        min_idx = i
inList[min_idx] = mmax
inList[max_idx] = mmin
print(' '.join(map(str, inList)))
