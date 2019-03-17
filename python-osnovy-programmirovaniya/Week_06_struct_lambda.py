# inList = list(map(int, input().split()))
# print(' '.join(map(str, inList)))

# Даны два целочисленных списка A и B, упорядоченных по неубыванию.
# Объедините их в один упорядоченный список С (то есть он должен содержать len(A)+len(B) элементов).
# Решение оформите в виде функции merge(A, B), возвращающей новый список.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Модифицировать исходные списки запрещается.
# Использовать функцию sorted и метод sort запрещается.
# inList1 = list(map(int, input().split()))
# inList2 = list(map(int, input().split()))
#
#
# def merge(a, b):
#     c = []
#     i, j = 0, 0
#     for k in range(len(a) + len(b)):
#         if i < len(a) and j < len(b):
#             if a[i] < b[j]:
#                 c.append(a[i])
#                 i += 1
#             else:
#                 c.append(b[j])
#                 j += 1
#         elif i < len(a):
#             c.append(a[i])
#             i += 1
#         elif j < len(b):
#             c.append(b[j])
#             j += 1
#     return c
#
#
# print(' '.join(map(str, merge(inList1, inList2))))

# Отсортируйте данный массив, используя встроенную сортировку.
# yoba = input()
# inList = list(map(int, input().split()))
# inList.sort()
# print(*inList)

# Системный администратор вспомнил, что давно не делал архива пользовательских файлов.
# Однако, объем диска, куда он может поместить архив,
# может быть меньше чем суммарный объем архивируемых файлов.
# Известно, какой объем занимают файлы каждого пользователя.
# Напишите программу, которая по заданной информации о пользователях и свободному объему
# на архивном диске определит максимальное число пользователей, чьи данные можно поместить в архив.
# inListSizeUsers = list(map(int, input().split()))
# size = inListSizeUsers[0]
# n = inListSizeUsers[1]
# u = []
# for i in range(n):
#     u.append(int(input()))
# u.sort()
# tt = 0
# i = 0
# while n != 0 and i < n and tt + u[i] < size:
#     tt += u[i]
#     i += 1
# print(i)

# Штаб гражданской обороны Тридесятой области решил обновить план спасения на случай ядерной атаки.
# Известно, что все n селений Тридесятой области находятся вдоль одной прямой дороги.
# Вдоль дороги также расположены m бомбоубежищ,
# в которых жители селений могут укрыться на случай ядерной атаки.
# Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее,
# необходимо для каждого селения определить ближайшее к нему бомбоубежище.
# n = int(input())
# np = list(map(int, input().split()))
# # Здесь создали 3-е поле для номера бомбоубежища
# for i in range(n):
#     np[i] = [np[i], i + 1, 0]
# np.sort()
#
# m = int(input())
# bu = list(map(int, input().split()))
# for i in range(m):
#     bu[i] = [bu[i], i + 1]
# bu.sort()
#
# # Переменная для начала вложенного цикла
# start = 0
# for i in range(n):
#     # Точка нахождения нужного бомбоубежища
#     idx = 0
#     # Чтобы минимум был точно больше любого найденного
#     minimum = 10e10
#     for j in range(start, m):
#         tmp = abs(np[i][0] - bu[j][0])
#         # Либо обновляем минимум и номер бомбоубежища
#         if tmp < minimum:
#             idx = j
#             minimum = tmp
#             np[i][2] = bu[j][1]
#         # Либо заканчиваем цикл
#         else:
#             break
#     # Переопределяем начало вложенного цикла
#     start = idx
#
# np.sort(key=lambda idx: idx[1])
# # print(*np)
# for i in range(len(np)):
#     print(np[i][2], end=" ")

# Чтение/ запись
# inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
# for line in inFile:
#     print(line[-2::-1], file=outFile)
# inFile.close()
# outFile.close()

# Известно, что фамилии всех участников — различны.
# Сохраните в массивах список всех участников и выведите его,
# отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.
# inFile = open('input.txt', 'r', encoding='utf8')
# lst = []
# for line in inFile:
#     lst.append(line.split())
# inFile.close()
# lst.sort()
# for i in lst:
#     print(i[0], i[1], i[3], sep=' ')

# Сортировка подсчетом. Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.
#
#
# def CountSort(A):
#     counts = [0 for i in range(101)]
#     for i in A:
#         counts[i] += 1
#     k = 0
#     for i in range(101):
#         for j in range(counts[i]):
#             A[k] = i
#             k += 1
#     return A
#
#
# lst = list(map(int, input().split()))
# print(' '.join(map(str, CountSort(lst))))

# В олимпиаде участвовало N человек.
# Каждый получил определенное количество баллов, при этом оказалось,
# что у всех участников разное число баллов.
# Упорядочите список участников олимпиады в порядке убывания набранных баллов.
# n = int(input())
# lst = []
# for i in range(n):
#     line = input().split()
#     lst.append([int(line[1]), line[0]])
# lst.sort(reverse=True)
# # for i in range(len(lst)):
# #     print(lst[i][1])
# print(*lst)


#
myInput = open("input.txt", "r", encoding="utf8")
myOutput = open("output.txt", "w", encoding="utf8")
k = int(myInput.readline())
myList = []
for line in myInput:
    newLine = line.split()
    if int(newLine[-1]) >= 40 and int(newLine[-2]) >= 40 \
            and int(newLine[-3]) >= 40:
        myList.append(newLine)
myInput.close()
myList.sort(key=lambda a: int(a[-1]) + int(a[-2]) + int(a[-3]))
myList.reverse()
konk = []
for i in myList:
    sum = int(i[-1]) + int(i[-2]) + int(i[-3])
    konk.append(sum)
n = len(konk)


def konkurs(n, k, konk):
    if n <= k:
        return 0
    elif konk[k] == konk[0]:
        return 1
    for i in range(k, 0, -1):
        if konk[i] < konk[i - 1]:
            return konk[i - 1]


print(konkurs(n, k, konk), file=myOutput)
myInput.close()
myOutput.close()