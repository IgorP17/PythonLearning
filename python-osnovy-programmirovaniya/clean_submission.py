# Мороженое продают по 3 и по 5 шариков, можно ли купить k шариков
n = int(input())
if n % 3 == 0 or n % 5 == 0 or n % 8 == 0:
    print("YES")
else:
    print("NO")
