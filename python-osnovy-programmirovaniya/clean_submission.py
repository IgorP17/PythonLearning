import math
s = float(input())
r = math.floor(s)
k = math.ceil((s - r) * 100)
print(r, "{:02d}".format(k))
