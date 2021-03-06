# Вещественные числа
import math

# Даны длины сторон треугольника. Вычислите площадь треугольника.
# a = float(input())
# b = float(input())
# c = float(input())
# p = (a + b + c) / 2
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(s)

# По данному числу n вычислите сумму 1+(1 / 2²)+(1 / 3²)+...+(1 / n²).
# n = int(input())
# i = 2
# sum1 = 1
# while i <= n:
#     sum1 += 1 / (i ** 2)
#     i += 1
# print(sum1)

# Дано положительное действительное число X. Выведите его дробную часть.
# f = float(input())
# n = math.floor(f)
# print(f - n)

# Цена товара обозначена в рублях с точностью до копеек,
# то есть действительным числом с двумя цифрами после десятичной точки.
# Запишите в две целочисленные переменные стоимость товара
# в виде целого числа рублей и целого числа копеек и выведите их на экран
# import math
# s = float(input())
# r = math.floor(s)
# k = math.ceil((s - r) * 100)
# print(r, "{:02d}".format(k))
#
# rubles = float(input())
# kopeks = round(rubles * 100)
# print(*divmod(kopeks, 100))

# По российский правилам числа округляются до ближайшего целого числа,
# а если дробная часть числа равна 0.5, то число округляется вверх.
# Дано неотрицательное число x, округлите его по этим правилам.
# from math import floor, ceil
# x = float(input())
# if x - floor(x) < 0.5:
#     x = floor(x)
# else:
#     x = ceil(x)
# print(x)

# Процентная ставка по вкладу составляет P процентов годовых,
# которые прибавляются к сумме вклада.
# Вклад составляет X рублей Y копеек. Определите размер вклада через год
# p = int(input())
# x = int(input())
# y = int(input())
# money_before = 100 * x + y
# money_after = int(money_before * (100 + p) / 100)
# print(money_after // 100, money_after % 100)

# Даны действительные коэффициенты a, b, c, при этом a != 0.
# Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.
# a = float(input())
# b = float(input())
# c = float(input())
# di = b ** 2 - 4 * a * c
# if di > 0:
#     x1 = (-b + math.sqrt(di)) / (2 * a)
#     x2 = (-b - math.sqrt(di)) / (2 * a)
#     if x1 - int(x1) == 0.0:
#         x1 = int(x1)
#     if x2 - int(x2) == 0.0:
#         x2 = int(x2)
#     if x1 < x2:
#         print(x1, x2)
#     else:
#         print(x2, x1)
# elif di == 0:
#     x = -b / (2 * a)
#     print(x)

# Даны вещественные числа a, b, c, d, e, f. Известно, что система линейных уравнений:
# ax + by = e
# cx + dy = f
# имеет ровно одно решение. Выведите два числа x и y, являющиеся решением этой системы.
# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())
# f = float(input())
# if b != 0:
#     y = (c * e - a * f) / (b * c - a * d)
#     if c != 0:
#         x = (f - d * y) / c
#         if x - int(x) == 0.0:
#             x = int(x)
#         if y - int(y) == 0.0:
#             y = int(y)
#         print(x, y)
# else:
#     if a != 0:
#         x = (f * b - d * e) / (b * c - d * a)
#         if d != 0:
#             y = (f - c * x) / d
#             if x - int(x) == 0.0:
#                 x = int(x)
#             if y - int(y) == 0.0:
#                 y = int(y)
#             print(x, y)

# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами
# (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# В шестой строке выведите все символы с нечетными индексами,
# то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# В девятой строке выведите длину данной строки.
# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])
# print(len(s))

# Дана строка.
# Если в этой строке буква f встречается только один раз,
# выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего появления.
# Если буква f в данной строке не встречается, ничего не выводите.
# При решении этой задачи нельзя использовать метод count и циклы.
# s = input()
# left = s.find("f")
# right = s.rfind("f")
# if left == right != -1:
#     print(left)
# elif left != -1:
#     print(left)
#     print(right)

# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними.
# s = input()
# left = s.find("h")
# right = s.rfind("h")
# print(s[:left], s[right + 1:], sep="")

# Дана строка.
# Найдите в этой строке второе вхождение буквы f
# и выведите индекс этого вхождения.
# Если буква f в данной строке встречается только один раз,
# выведите число -1,
# а если не встречается ни разу, выведите число -2.
# При решении этой задачи нельзя использовать метод count.
# s = input()
# n1 = s.find("f")
# if n1 == -1:
#     print(-2)
# else:
#     n2 = s.find("f", n1 + 1)
#     if n2 == -1:
#         print(-1)
#     else:
#         print(n2)

# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.
# При решении этой задачи нельзя пользоваться циклами и инструкцией if.
# s = input()
# n = s.find(" ")
# print(s[n + 1:], s[:n])

# Дана строка,
# состоящая из слов,
# разделенных пробелами.
# Определите, сколько в ней слов.
# s = input()
# print(s.count(" ") + 1)

# Дана строка. Замените в этой строке все цифры 1 на слово one.
# s = input()
# print(s.replace("1", "one"))

# Дана строка. Удалите из этой строки все символы @.
s = input()
print(s.replace("@", ""))