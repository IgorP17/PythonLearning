n = int(input())
if 10 < n < 20:
    if n % 10 == 0:
        print(n, "korov")
    if n % 10 == 5:
        print(n, "korov")
    if n % 10 == 6:
        print(n, "korov")
    if n % 10 == 7:
        print(n, "korov")
    if n % 10 == 8:
        print(n, "korov")
    if n % 10 == 9:
        print(n, "korov")
elif n % 10 == 1:
    print(n, "korova")
else:
    print(n, "korovy")
