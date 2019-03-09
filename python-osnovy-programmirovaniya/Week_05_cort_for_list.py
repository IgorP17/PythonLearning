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
inList = list(map(int, input().split()))
mn = 1001
for i in range(len(inList)):
    if 0 < inList[i] < mn:
        mn = inList[i]
print(mn)
