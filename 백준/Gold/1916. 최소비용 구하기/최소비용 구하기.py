import sys
input = sys.stdin.readline
from heapq import *

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
INF = int(10e9)
distance = [INF] * (N + 1)
start, end = map(int, input().split())
def dijkstra(start):
    distance[start] = 0
    queue = []
    heappush(queue, (0, start))
    while queue:
        dist, now = heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(queue, (cost, i[0]))
dijkstra(start)
print(distance[end])