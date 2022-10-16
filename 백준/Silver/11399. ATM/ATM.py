import sys
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
people.sort()
# 1 2 3 4 4
cnt = 0
for i in range(len(people)):
    cnt += sum(people[:i+1])
print(cnt)