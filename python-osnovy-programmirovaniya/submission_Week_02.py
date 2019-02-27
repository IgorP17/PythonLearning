# MAX if
# n = int(input())
# m = int(input())
# if n > m:
#     print(n)
# else:
#     print(m)

# Compare
# n = int(input())
# m = int(input())
# if n > m:
#     print(1)
# elif n < m:
#     print(2)
# else:
#     print(0)

# MAX 3
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# mx = n1
# if n2 > mx:
#     mx = n2
# if n3 > mx:
#     mx = n3
# print(mx)

# Високосный год
# n = int(input())
# if (n % 4 == 0 and n % 100 > 0) or n % 400 == 0:
#     print("YES")
# else:
#     print("NO")

# Ход короля
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
#     print("YES")
# else:
#     print("NO")

# Одинаковые клетки шахшатной доски
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# Цвет одинаков если
# 1. Смещение по Х кратно 2 И смещение по Y кратно 2
# 2. Смещение по Х не кратно 2 И смещение по Y не кратно 2
# isEven = (abs(x1 - x2) % 2 == 0) and (abs(y1 - y2) % 2 == 0)
# isOdd = (abs(x1 - x2) % 2 != 0) and (abs(y1 - y2) % 2 != 0)
# if isEven or isOdd:
#     print("YES")
# else:
#     print("NO")

# Шоколодка N x M, возможно ли отломить K долек
# n = int(input())
# m = int(input())
# k = int(input())
# isYes = 0
# for i in range(n):
#     if (i + 1) * m == k:
#         isYes = 1
# for j in range(m):
#     if (j + 1) * n == k:
#         isYes = 1
# if isYes == 1:
#     print("YES")
# else:
#     print("NO")

# Знак числа
# n = int(input())
# sign = 0
# if n > 0:
#     sign = 1
# elif n < 0:
#     sign = -1
# else:
#     sign = 0
# print(sign)

# 2 точки в одной четверти
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# isYes = 0
# if (x1 > 0 and x2 > 0) and ((y1 > 0 and y2 > 0) or (y1 < 0 and y2 < 0)):
#     isYes = 1
# if (x1 < 0 and x2 < 0) and ((y1 > 0 and y2 > 0) or (y1 < 0 and y2 < 0)):
#     isYes = 1
# if isYes == 1:
#     print("YES")
# else:
#     print("NO")

# 3 числа - в них есть чет и нечет
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# isEven1 = n1 % 2 == 0
# isEven2 = n2 % 2 == 0
# isEven3 = n3 % 2 == 0
# isEvenTotal = isEven1 or isEven2 or isEven3
# isOddTotal = not isEven1 or not isEven2 or not isEven3
# if isEvenTotal and isOddTotal:
#     print("YES")
# else:
#     print("NO")

# Совпадение чисел
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# eq = 0
# if n1 == n2 and n2 == n3:
#     eq = 3
# elif n1 == n2 and n1 != n3:
#     eq = 2
# elif n1 == n3 and n1 != n2:
#     eq = 2
# elif n2 == n3 and n2 != n1:
#     eq = 2
# print(eq)

# Мороженое продают по 3 и по 5 шариков, можно ли купить k шариков
# n = int(input())
# n2 = n
# result = 0
# while n > 0:
#     if n % 3 == 0:
#         result = 1
#         break
#     else:
#         n = n - 5
# n = n2
# if result == 0:
#     while n > 0:
#         if n % 5 == 0:
#             result = 1
#             break
#         else:
#             n = n - 3
# print("YES" if result == 1 else "NO")

# Упорядочить 3 числа
# a, b, c = int(input()), int(input()), int(input())
# while a > b or b > c:
#     if a > b:
#         (a, b) = (b, a)
#     if b > c:
#         (b, c) = (c, b)
# print(a, b, c, sep=" ")

# N КОРОВ
# Здесь собраны правила склонения слова "корова" (n < 100).
#
#     "n коров", если 10 < n < 20 или последняя цифра n - одна из 0, 5, 6, 7, 8, 9.
#     "n корова", если последняя цифра n == 1.
#     "n коровы" во всех остальных случаях.
# n = int(input())
# if 10 < n < 20:
#     print(n, "korov")
# elif n % 10 == 0:
#     print(n, "korov")
# elif n % 10 == 5:
#     print(n, "korov")
# elif n % 10 == 6:
#     print(n, "korov")
# elif n % 10 == 7:
#     print(n, "korov")
# elif n % 10 == 8:
#     print(n, "korov")
# elif n % 10 == 9:
#     print(n, "korov")
# elif n % 10 == 1:
#     print(n, "korova")
# else:
#     print(n, "korovy")

# За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D×E.
# Замок Иф сложен из кирпичей, размером A×B×C.
# Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие
# (очевидно, стороны кирпича должны быть параллельны сторонам отверстия).
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= d and b <= e:
    print("YES")
elif b <= d and a <= e:
    print("YES")
elif a <= d and c <= e:
    print("YES")
elif c <= d and a <= e:
    print("YES")
elif c <= d and b <= e:
    print("YES")
elif b <= d and c <= e:
    print("YES")
else:
    print("NO")
