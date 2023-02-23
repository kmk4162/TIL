import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
parent = [i for i in range(N)] # [0,1,2,3,4,5]

# 부모를 찾기위해 계속 재귀하는 함수
def find(x):
    # 그냥 하면 O(N) 방식으로 비효율적
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

# 두 집합을 합치는 함수
def union(a, b):
    a = find(a)
    b = find(b)
    if parent[a] < parent[b]:
        parent[parent[a]] = parent[b]
    else:
        parent[parent[b]] = parent[a]

cnt = 0
for i in range(M):
    cnt += 1
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(cnt)
        exit()
    union(a, b)
else:
    print(0)