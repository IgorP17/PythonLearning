

def MinDivisor(n):
    k = int(n ** 0.5) + 1
    i = 2
    while i < k:
        if n % i == 0:
            return i
        i += 1
    return n


n = int(input())
print(MinDivisor(n))
