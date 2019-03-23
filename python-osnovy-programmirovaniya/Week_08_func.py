# filter()
# enumerate
# any()
# all()
# zip()
# import itertools
# import functools
# itertools.combinations()
# itertools.permutations()

# Дан список чисел, который может содержать до 100000 чисел.
# Определите, сколько в нем встречается различных чисел.
# print(len(set(input().split())))

# Во входном файле (вы можете читать данные из sys.stdin,
# подключив библиотеку sys) записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
# import sys
# print(len(set(str(sys.stdin.read()).split())))

# Выведите значение наименьшего нечетного элемента списка,
# гарантируется, что хотя бы один нечётный элемент в списке есть.
# print(
#     min(
#         list
#         (filter
#          (lambda f: f % 2 != 0,
#           map(int, input().split()))
#          )
#     )
# )

# Проверьте, есть ли среди данных N чисел нули.
# print(True in set(map(lambda x: int(input()) == 0, range(int(input())))))

# На вход подаётся последовательность натуральных чисел длины n≤1000.
# Посчитайте произведение пятых степеней чисел в последовательности.
# import functools
#
# print(
#     functools.reduce(
#         lambda a, b: a * b,
#         map(
#             lambda p5: p5 ** 5,
#             map(int, input().split()))
#     )
# )

# Булева функция XOR
print(' '.join(map(lambda a, b: str(int(a != b)), input().split(), input().split())))
