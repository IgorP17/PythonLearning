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
