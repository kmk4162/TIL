import sys
input = sys.stdin.readline

N, k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort(reverse = True)
print(scores[k-1])