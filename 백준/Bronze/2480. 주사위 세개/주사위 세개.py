a, b, c = map(int, input().split())

if a == b == c:
    prize = (10000+ 1000 * a)
elif a == b != c:
    prize = (1000+ 100 * a)
elif a == c != b:
    prize = (1000+ 100 * a)
elif b == c != a:
    prize = (1000 + 100 * b)
else:
    list1 = [a, b, c]
    list1.sort()
    prize = list1[2] * 100

print(prize)

