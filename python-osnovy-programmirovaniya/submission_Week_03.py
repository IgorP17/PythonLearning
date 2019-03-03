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
