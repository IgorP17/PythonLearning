# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
# которая не содержит инструкции if,
# а использует стандартную функцию min от двух чисел.
# Считайте четыре целых числа и выведите их минимум.
#
#
# def min4(a1, b1, c1, d1):
#     return min(a1, b1, c1, d1)
#
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(min4(a, b, c, d))

# Даны четыре действительных числа: x₁, y₁, x₂, y₂.
# Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точками (x₁,y₁) и (x₂,y₂).
# Считайте четыре действительных числа и выведите результат работы этой функции.
#
#
# def distance(a1, b1, a2, b2):
#     dist = ((a1 - a2) ** 2 + (b1 - b2) ** 2) ** 0.5
#     if dist - int(dist) == 0.0:
#         dist = int(dist)
#     return dist
#
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# print(distance(x1, y1, x2, y2))

# Даны два действительных числа x и y.
# Проверьте, принадлежит ли точка с координатами (x,y) заштрихованному квадрату (включая его границу).
# Если точка принадлежит квадрату, выведите слово YES, иначе выведите слово NO.
# На рисунке сетка проведена с шагом 1 (КВАДРАТ -1 -1 --0-- 1 1).
# Решение должно содержать функцию IsPointInSquare(x, y), возвращающую True,
# если точка принадлежит квадрату и False, если не принадлежит.
# Основная программа должна считать координаты точки,
# вызвать функцию IsPointInSquare и в зависимости от возвращенного значения вывести на экран необходимое сообщение.
# Функция IsPointInSquare не должна содержать инструкцию if.
#
#
# def isPointInSquare(x1, y1):
#     return -1.0 <= x1 <= 1.0, -1.0 <= y1 <= 1.0
#
#
# x = float(input())
# y = float(input())
# print("YES" if str(isPointInSquare(x, y)) == "(True, True)" else "NO")

# Даны пять действительных чисел: x, y, xc, yc, r.
# Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r.
# Если точка принадлежит кругу, выведите слово YES, иначе выведите слово NO.
# Решение должно содержать функцию IsPointInCircle(x, y, xc, yc, r),
# возвращающую True, если точка принадлежит кругу и False, если не принадлежит.
# Основная программа должна считать координаты точки, вызвать функцию IsPointInCircle
# и в зависимости от возвращенного значения вывести на экран необходимое сообщение.
# Функция IsPointInCircle не должна содержать инструкцию if.
#
#
# def IsPointInCircle(x, y, xc, yc, r):
#     return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2
#
#
# x = float(input())
# y = float(input())
# xc = float(input())
# yc = float(input())
# r = float(input())
# print("YES" if str(IsPointInCircle(x, y, xc, yc, r)) == "True" else "NO")

# Дано натуральное число n>1.
# Выведите его наименьший делитель, отличный от 1.
# Решение оформите в виде функции MinDivisor(n).
# Алгоритм должен иметь сложность порядка корня квадратного из n.
# Указание. Если у числа n нет делителя не превосходящего корня из n,
# то число n — простое и ответом будет само число n.
# А у всех составных чисел обязательно есть делители,
# отличные от единицы и не превосходящие корня из n.
#
#
# def MinDivisor(n):
#     k = int(n ** 0.5) + 1
#     i = 2
#     while i < k:
#         if n % i == 0:
#             return i
#         i += 1
#     return n
#
#
# n = int(input())
# print(MinDivisor(n))

# Дано натуральное число n>1.
# Проверьте, является ли оно простым.
# Программа должна вывести слово YES, если число простое и NO, если число составное.
# Решение оформите в виде функции IsPrime(n),
# которая возвращает True для простых чисел и False для составных чисел.
# Программа должна иметь сложность O(корень из n):
# количество действий в программе должно быть пропорционально квадратному корню из n
# (иначе говоря, при увеличении входного числа в k раз,
# время выполнения программы должно увеличиваться примерно в корень из k раз).
#
#
# def isPrime(n_f):
#     k = int(n_f ** 0.5) + 1
#     i = 2
#     while i < k:
#         if n_f % i == 0:
#             return "NO"
#         i += 1
#     return "YES"
#
#
# n = int(input())
# print(isPrime(n))

# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите aⁿ, не используя циклы и стандартную функцию pow, но используя рекуррентное соотношение aⁿ=a⋅aⁿ⁻¹.
# Решение оформите в виде функции power(a, n) (которая возвращает aⁿ).


# def power(a1, n1):
#     if n1 == 0:
#         return 1
#     if n1 == 1:
#         if a1 - int(a1) == 0.0:
#             return int(a1)
#         return a1
#     else:
#         result = a1 * power(a1, n1 - 1)
#         if result - int(result) == 0.0:
#             result = int(result)
#         return result
#
#
# a = float(input())
# n = int(input())
# print(power(a, n))

# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.


def adds(a1, b1):
    if a1 == 0:
        return b1
    return adds(a1 - 1, b1 + 1)


a = int(input())
b = int(input())
print(adds(a, b))
