myInput = open("input.txt", "r", encoding="utf8")
myOutput = open("output.txt", "w", encoding="utf8")
k = int(myInput.readline())
myList = []
for line in myInput:
    newLine = line.split()
    if int(newLine[-1]) >= 40 and int(newLine[-2]) >= 40 \
            and int(newLine[-3]) >= 40:
        myList.append(newLine)
myInput.close()
myList.sort(key=lambda a: int(a[-1]) + int(a[-2]) + int(a[-3]))
myList.reverse()
konk = []
for i in myList:
    mySum = int(i[-1]) + int(i[-2]) + int(i[-3])
    konk.append(mySum)
n = len(konk)


def konkurs(n1, k1, konk1):
    if n1 <= k1:
        return 0
    elif konk1[k1] == konk1[0]:
        return 1
    for i in range(k1, 0, -1):
        if konk1[i] < konk1[i - 1]:
            return konk1[i - 1]


print(konkurs(n, k, konk), file=myOutput)
myInput.close()
myOutput.close()
