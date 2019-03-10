inList1 = list(map(int, input().split()))
inList2 = list(map(int, input().split()))


def merge(a, b):
    c = []
    i, j = 0, 0
    for k in range(len(a) + len(b)):
        if i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        elif i < len(a):
            c.append(a[i])
            i += 1
        elif j < len(b):
            c.append(b[j])
            j += 1
    return c


print(' '.join(map(str, merge(inList1, inList2))))
