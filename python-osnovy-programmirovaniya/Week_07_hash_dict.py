# Дан список чисел, который может содержать до 100000 чисел.
# Определите, сколько в нем встречается различных чисел.
# inList = list(map(int, input().split()))
# mn = set(inList)
# print(len(mn))

# Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
# Выведите все числа, которые входят как в первый,
# так и во второй список, в порядке возрастания.

# print(' '.join(map(str, set(list(map(int, input().split()))) & set(list(map(int, input().split()))))))
# res = set(list(map(int, input().split()))) & set(list(map(int, input().split())))
# res = list(res)
# res.sort()
# print(' '.join(map(str, res)))

# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.
# inList = list(map(int, input().split()))
# occured = set([])
# result = []
# for i in range(len(inList)):
#     if inList[i] in occured:
#         result.append('YES')
#     else:
#         result.append('NO')
#         occured.add(inList[i])
# for i in result:
#     print(i)

# Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку sys)
# записан текст. Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
# import sys
# txt = sys.stdin.read()
# lst = str(txt).split()
# mn = set(lst)
# print(len(mn))

# Август и Беатриса играют в игру.
# Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ею чисел есть задуманное или NO в противном случае.
# После нескольких заданных вопросов Беатриса запуталась в том,
# какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить,
# какие числа мог задумать Август.
#
# Формат ввода
# Первая строка входных данных содержит число n — наибольшее число, которое мог загадать Август.
# Далее идут строки, содержащие вопросы Беатрисы.
# Каждая строка представляет собой набор чисел, разделенных пробелами.
# После каждой строки с вопросом идет ответ Августа: YES или NO.
# Наконец, последняя строка входных данных содержит одно слово HELP.
# n = int(input())
# allNum = set(range(1, n + 1))
# while True:
#     quest = input()
#     if quest == 'HELP':
#         break
#     quest = {int(x) for x in quest.split()}
#     answer = input()
#     if answer == 'YES':
#         allNum &= quest
#     if answer == 'NO':
#         allNum -= quest
# print(' '.join([str(x) for x in sorted(allNum)]))

# Каждый из N школьников некоторой школы знает Mᵢ языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# INPUT:
# 3
# 3
# Russian
# English
# Japanese
# 2
# Russian
# English
# 1
# English
# union = set()
# allLang = set()
# for i in range(int(input())):
#     m = int(input())
#     a = {input() for j in range(m)}
#     allLang.update(a)
#     if i == 1:
#         union.update(a)
#     else:
#         union &= a
# print(len(union))
# print('\n'.join(sorted(union)))
# print(len(allLang))
# print('\n'.join(sorted(allLang)))

# На Новом проспекте для разгрузки было решено пустить два новых автобусных маршрута на разных участках проспекта.
# Известны конечные остановки каждого из автобусов.
# Определите количество остановок, на которых можно пересесть с одного автобуса на другой.
# inList = list(map(int, input().split()))
# if inList[0] > inList[1]:
#     (inList[0], inList[1]) = (inList[1], inList[0])
# if inList[2] > inList[3]:
#     (inList[2], inList[3]) = (inList[3], inList[2])
# # множество
# bus1 = set(range(inList[0], inList[1] + 1))
# bus2 = set(range(inList[2], inList[3] + 1))
# # print(*bus1)
# # print(*bus2)
# res = bus1 & bus2
# print(len(res))

# Словарь
# in
# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa
# out
# 7
# baca - fruit
# bacca - fruit
# malum - apple, punishment
# multa - punishment
# pomum - apple
# popula - apple
# popum - fruit
# n = int(input())
# latinEnglish = {}
# for i in range(n):
#     line = input()
#     english = line[:line.find('-')].strip()
#     latinsStr = line[line.find('-') + 1:].strip()
#     latins = map(lambda s: s.strip(), latinsStr.split(','))
#     for latin in latins:
#         if latin not in latinEnglish:
#             latinEnglish[latin] = []
#         latinEnglish[latin].append(english)
# print(len(latinEnglish))
# for latin in sorted(latinEnglish):
#     print(latin, '-', ', '.join(sorted(latinEnglish[latin])))

# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# inFile = open("input.txt", "r", encoding="utf8")
# reader = inFile.read().split()
# words = dict({})
# occurs = []
# for word in reader:
#     # если слово уже встречалось
#     if word in words:
#         # обновим значение словаря
#         words[word] += 1
#         # добавим значение в наблюдаемое
#         occurs.append(words[word])
#     # иначе надо занести
#     else:
#         words[word] = 0
#         # и добавить в наблюдаемое
#         occurs.append(0)
# print(*occurs)

# Вам дан словарь, состоящий из пар слов.
# Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для одного данного слова определите его синоним.
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
# Кю - может быть задание не правой, а левой части
# n = int(input())
# fwrd = dict({})
# bkwrd = dict({})
# for i in range(n):
#     (a, b) = input().split()
#     fwrd[a] = b
#     bkwrd[b] = a
# kword = input()
# # ищем в прямом словаре
# if kword in fwrd:
#     print(fwrd[kword])
# # иначе ищем в обратном
# elif kword in bkwrd:
#     print(bkwrd[kword])

# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# oh you touch my tralala mmm my ding ding dong
# Вывод программы:
# ding
# import sys
#
# txt = sys.stdin.read()
# lst = str(txt).split()
# myDict = dict({})
# # идем по словам
# for i in lst:
#     # если слово встречалось
#     if i in myDict:
#         myDict[i] += 1
#     # а если нет, то заведем
#     else:
#         myDict[i] = 1
# # добавим в список в обратном порядке ключ значение
# revLst = []
# for i in myDict:
#     revLst.append((myDict[i], i))
# revLst.sort(reverse=True)
# cnt = revLst[0][0]
# word = revLst[0][1]
# for i in range(len(revLst)):
#     if revLst[i][0] >= cnt and revLst[i][1] < word:
#         word = revLst[i][1]
# print(word)

# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.
import sys

txt = sys.stdin.read()
lst = str(txt).split()
myDict = dict({})
# идем по словам
for i in lst:
    # если слово встречалось
    if i in myDict:
        myDict[i] += 1
    # а если нет, то заведем
    else:
        myDict[i] = 1
# добавим в список в обратном порядке ключ значение
lst = []
for i in myDict:
    lst.append((myDict[i], i))
# магия лямбды
lst.sort(key=lambda word: (-word[0], word[1]))
for i in lst:
    print(i[1])

