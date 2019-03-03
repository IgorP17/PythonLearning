import math
a = float(input())
b = float(input())
c = float(input())
di = b ** 2 - 4 * a * c
if di > 0:
    x1 = (-b + math.sqrt(di)) / (2 * a)
    x2 = (-b - math.sqrt(di)) / (2 * a)
    if x1 - int(x1) == 0.0:
        x1 = int(x1)
    if x2 - int(x2) == 0.0:
        x2 = int(x2)
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
elif di == 0:
    x = -b / (2 * a)
    print(x)
