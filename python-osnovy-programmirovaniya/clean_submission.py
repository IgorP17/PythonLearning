# 3 числа - в них есть чет и нечет
n1 = int(input())
n2 = int(input())
n3 = int(input())
isEven1 = n1 % 2 == 0
isEven2 = n2 % 2 == 0
isEven3 = n3 % 2 == 0
isEvenTotal = isEven1 or isEven2 or isEven3
isOddTotal = not isEven1 or not isEven2 or not isEven3
if isEvenTotal and isOddTotal:
    print("YES")
else:
    print("NO")
