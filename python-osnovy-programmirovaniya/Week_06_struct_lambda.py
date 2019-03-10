# inList = list(map(int, input().split()))
# print(' '.join(map(str, inList)))

# Даны два целочисленных списка A и B, упорядоченных по неубыванию.
# Объедините их в один упорядоченный список С (то есть он должен содержать len(A)+len(B) элементов).
# Решение оформите в виде функции merge(A, B), возвращающей новый список.
# Алгоритм должен иметь сложность O(len(A)+len(B)).
# Модифицировать исходные списки запрещается.
# Использовать функцию sorted и метод sort запрещается.
inList1 = list(map(int, input().split()))
inList2 = list(map(int, input().split()))


def merge(a, b):
    result = a + b
    return sort(result)


def sort(zzz):
    z = zzz.copy()
    for i in range(len(z) - 1):
        for j in range(i, len(z)):
            if z[i] >= z[j]:
                z[i], z[j] = z[j], z[i]
    return z


print(' '.join(map(str, merge(inList1, inList2))))
