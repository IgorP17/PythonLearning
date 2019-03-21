inFile = open("input.txt", "r", encoding="utf8")
reader = inFile.read().split()
words = dict({})
occurs = []
for word in reader:
    # если слово уже встречалось
    if word in words:
        # обновим значение словаря
        words[word] += 1
        # добавим значение в наблюдаемое
        occurs.append(words[word])
    # иначе надо занести
    else:
        words[word] = 0
        # и добавить в наблюдаемое
        occurs.append(0)
print(*occurs)
