

def power(a1, n1):
    if n1 == 0:
        return 1
    if n1 == 1:
        if a1 - int(a1) == 0.0:
            return int(a1)
        return a1
    else:
        result = a1 * power(a1, n1 - 1)
        if result - int(result) == 0.0:
            result = int(result)
        return result


a = float(input())
n = int(input())
print(power(a, n))
