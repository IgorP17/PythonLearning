inList1 = list(map(int, input().split()))
inList2 = list(map(int, input().split()))


def merge(a, b):
    result = a + b
    return sort(result)


def sort(z):
    for i in range(len(z) - 1):
        for j in range(i, len(z)):
            if z[i] >= z[j]:
                z[i], z[j] = z[j], z[i]
    return z


print(' '.join(map(str, merge(inList1, inList2))))
