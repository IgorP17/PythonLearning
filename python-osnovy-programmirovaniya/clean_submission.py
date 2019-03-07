

def adds(a1, b1):
    if a1 == 0:
        return b1
    return adds(a1 - 1, b1 + 1)


a = int(input())
b = int(input())
print(adds(a, b))
