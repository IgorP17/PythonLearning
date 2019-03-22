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
revLst = []
for i in myDict:
    revLst.append((myDict[i], i))
revLst.sort(reverse=True)
cnt = revLst[0][0]
word = revLst[0][1]
for i in range(len(revLst)):
    if revLst[i][0] >= cnt and revLst[i][1] < word:
        word = revLst[i][1]
print(word)
