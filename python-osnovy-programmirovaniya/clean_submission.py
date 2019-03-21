n = int(input())
fwrd = dict({})
bkwrd = dict({})
for i in range(n):
    (a, b) = input().split()
    fwrd[a] = b
    bkwrd[b] = a
kword = input()
# ищем в прямом словаре
if kword in fwrd:
    print(fwrd[kword])
# иначе ищем в обратном
elif kword in bkwrd:
    print(bkwrd[kword])
