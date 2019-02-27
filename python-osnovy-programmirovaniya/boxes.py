# 2 коробки
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
# упорядочить по убыванию
while a1 < b1 or b1 < c1:
    if a1 < b1:
        (a1, b1) = (b1, a1)
    if b1 < c1:
        (b1, c1) = (c1, b1)
while a2 < b2 or b2 < c2:
    if a2 < b2:
        (a2, b2) = (b2, a2)
    if b2 < c2:
        (b2, c2) = (c2, b2)
# print(a1, b1, c1)
# print(a2, b2, c2)
# Равны
if a1 == a2 and b1 == b2 and c1 == c2:
    print("Boxes are equal")
# а теперь первая меньше
elif a1 <= a2 and b1 <= b2 and c1 < c2:
    print("The first box is smaller than the second one")
# а теперь первая больше
elif a1 >= a2 and b1 >= b2 and c1 > c2:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
