import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()
answer = 0
while True:
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]
    if S == T:
        answer = 1
        break
    if len(T) == 0:
        break
print(answer)