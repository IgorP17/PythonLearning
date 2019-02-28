n = int(input())
value = n
counter = 1
max1 = 1
while n != 0:
    n = int(input())
    if n == value:
        counter += 1
        if counter > max1:
            max1 = counter
        # counter <
    else:
        value = n
        counter = 1
print(max1)
