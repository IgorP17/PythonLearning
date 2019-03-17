import sys
txt = sys.stdin.read()
lst = str(txt).split()
mn = set(lst)
print(len(mn))
