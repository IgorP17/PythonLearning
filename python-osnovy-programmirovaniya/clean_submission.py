inList = list(map(int, input().split()))
if inList[0] > inList[1]:
    (inList[0], inList[1]) = (inList[1], inList[0])
if inList[2] > inList[3]:
    (inList[2], inList[3]) = (inList[3], inList[2])
# множество
bus1 = set(range(inList[0], inList[1] + 1))
bus2 = set(range(inList[2], inList[3] + 1))
# print(*bus1)
# print(*bus2)
res = bus1 & bus2
print(len(res))
