inFile = open("input.txt", "r", encoding="utf8")
outFile = open('output.txt', 'w', encoding='utf8')
reader = inFile.readlines()
dct = dict({})
cnt = 0
for i in reader:
    # удалим перевод строки
    ln = i.strip()
    if ln in dct:
        dct[ln] += 1
    else:
        dct[ln] = 1
    cnt += 1
lst = []
for i in dct:
    lst.append((dct[i], i))
# магия лямбды
lst.sort(key=lambda word: (-word[0], word[1]))
if lst[0][0] * 100 / cnt > 50:
    print(lst[0][1], file=outFile)
else:
    print(lst[0][1], file=outFile)
    print(lst[1][1], file=outFile)
inFile.close()
outFile.close()
