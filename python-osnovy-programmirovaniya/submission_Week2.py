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
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == 1 or abs(y1 - y2) == 1:
    print("YES")
else:
    print("NO")
