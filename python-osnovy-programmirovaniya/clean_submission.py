inListSizeUsers = list(map(int, input().split()))
size = inListSizeUsers[0]
n = inListSizeUsers[1]
u = []
for i in range(n):
    u.append(int(input()))
u.sort()
tt = 0
i = 0
while n != 0 and i < n and tt + u[i] < size:
    tt += u[i]
    i += 1
print(i)
