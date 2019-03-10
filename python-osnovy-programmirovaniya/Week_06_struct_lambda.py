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
