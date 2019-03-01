max1 = int(input())
tmp = int(input())
max2 = tmp
while tmp != 0:
    if tmp >= max1:
        max2, max1 = max1, tmp
    elif max2 < tmp <= max1:
        max2 = tmp
    tmp = int(input())
print(max2)
