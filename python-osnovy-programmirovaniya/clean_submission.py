inList = list(map(int, input().split()))
mmin = mmax = inList[0]
min_idx = max_idx = 0
for i in range(len(inList)):
    if inList[i] >= mmax:
        mmax = inList[i]
        max_idx = i
    elif inList[i] <= mmin:
        mmin = inList[i]
        min_idx = i
inList[min_idx] = mmax
inList[max_idx] = mmin
print(' '.join(map(str, inList)))
