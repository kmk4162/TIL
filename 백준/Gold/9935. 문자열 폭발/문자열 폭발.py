import sys
input = sys.stdin.readline

line = list(input().strip())
explosion = list(input().strip())

check = []
for char in line:
    check.append(char)
    if explosion == check[-len(explosion):]:
        for _ in range(len(explosion)):
            check.pop()

if check:
    print(''.join(check))
else:
    print('FRULA')