import sys
input = sys.stdin.readline

N = int(input())
result = []
cnt = 0
for i in range(N):
    cnt += 1
    age, name = input().split()
    result.append((int(age), name, cnt))
answer = sorted(result, key = lambda x : (x[0], x[2]))
for i in answer:
    print(i[0], i[1])