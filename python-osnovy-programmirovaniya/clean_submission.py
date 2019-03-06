

def isPrime(n_f):
    k = int(n_f ** 0.5) + 1
    i = 2
    while i < k:
        if n_f % i == 0:
            return "NO"
        i += 1
    return "YES"


n = int(input())
print(isPrime(n))
