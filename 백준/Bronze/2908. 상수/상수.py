a, b = map(str, input().split())

rev_a = list(a)[::-1]
rev_b = list(b)[::-1]

rev_a = int(''.join(rev_a))
rev_b = int(''.join(rev_b))

if rev_a > rev_b:
    print(rev_a)
else:
    print(rev_b)