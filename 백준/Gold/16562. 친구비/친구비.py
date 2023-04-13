import sys
input = sys.stdin.readline

N, M, k = map(int, input().split()) # 친구 그룹을 찾고, 그 그룹의 가장 최솟값들만 계산하기
parent = [i for i in range(N + 1)] # [0,1,2,3,4,5]
arr = [0] + list(map(int, input().split()))

# 부모를 찾기위해 계속 재귀하는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 집합을 합치는 함수
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        # 비용이 더 작은쪽으로 부모를 바꿔줌
        if arr[a] <= arr[b]: 
            parent[b] = a
        else:
            parent[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

cost = 0
for i in range(1, N + 1):
    if i == parent[i]:
        cost += arr[i]
if cost <= k:
    print(cost)
else:
    print('Oh no')