

def isPointInSquare(x1, y1):
    return -1.0 <= x1 <= 1.0, -1.0 <= y1 <= 1.0


x = float(input())
y = float(input())
print("YES" if str(isPointInSquare(x, y)) == "(True, True)" else "NO")
