max1 = n = int(input())
counter = 1
while n != 0:
    n = int(input())
    if n > max1:
        counter = 1
        max1 = n
    elif n == max1:
        counter += 1
print(counter)
