inList = list(map(int, input().split()))
mn = 1001
for i in range(len(inList)):
    if 0 < inList[i] < mn:
        mn = inList[i]
print(mn)
