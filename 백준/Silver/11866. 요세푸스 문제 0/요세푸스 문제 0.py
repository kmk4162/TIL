import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
numlist= deque(list(range(1, N + 1)))
answer = []

while numlist:
    for i in range(K - 1):
        numlist.append(numlist.popleft())

    answer.append(numlist.popleft())
print(str(answer).replace('[','<').replace(']','>'))