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

# Мороженое продают по 3 и по 5 шариков, можно ли купить k шариков WRONG
n = int(input())
if n % 3 == 0 or n % 5 == 0 or n % 8 == 0:
    print("YES")
else:
    print("NO")
