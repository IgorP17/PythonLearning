n = int(input())

# Электронные часы 2
# Если задали более суток вычленим
# n = n % 86400
# Часы
# hh = n // 3600
# Часы можно вычесть
# n = n - hh * 3600
# Минуты
# mm = n // 60
# n = n - mm * 60
# print(hh, ":", str(mm).zfill(2), ":", str(n).zfill(2), sep="")

# вторая цифра
# print((n % 100) // 10)

# сумма цифр 3х значного числа
# print(n // 100 + (n % 100) // 10 + n % 10)

# электронные часы
# print((n % 1440) // 60, (n % 1440) % 60)

# Стоимость покупки
# a = int(input())
# b = int(input())
# n = int(input())
# print(((a * 100 + b) * n) // 100, ((a * 100 + b) * n) % 100)

# 0 в 1, 1 в 0
# print(str(bin(n + 1))[-1:])

# округление вверх
# n = int(input())
# m = int(input())
# print((m + n - 1) // n)

# Симметричность
# n = input()
# n = n.zfill(4)
# revers = n[-1:] + n[-2:-1] + n[-3:-2] + n[-4:-3]
# print(1 if n.__eq__(revers) else 7)

# Кратность
# a = int(input())
# b = int(input())
# result = a % b == 0
# print('YES' * result + 'NO' * (1 - result))

# MAX
# a = int(input())
# b = int(input())
# result = a > b
# print(a * result + b * (1 - result))

# Улитка вверх днем, вниз ночью
# height = int(input())
# distUp = int(input())
# distDown = int(input())
# u = height - distUp
# d = distUp - distDown
# result = 1 + (u + d - 1) // d
# print(result)

# Следующее четное число
# n = int(input())
# n1 = (n + 2) if n % 2 == 0 else (n + 1)
# print(n1)
