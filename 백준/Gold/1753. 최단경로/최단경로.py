import sys
input = sys.stdin.readline
from heapq import *

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range (V + 1)]
INF = int(10e9)
distance = [INF] * (V + 1)
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
# print(graph)

def dijkstra(start):
    distance[start] = 0
    q = []
    heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로는 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] # 거리 더해주기
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == 10e9:
        print('INF')
    else:
        print(distance[i])