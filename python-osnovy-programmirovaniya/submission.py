# n = int(input())

# Электронные часы 2
# print((n % 86400) // 3600, ":", (n % 86400) // 60, ":", (n % 86400) % 3600, sep="")

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
