import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N):
    line = input().strip()
    graph.append(line)

K = int(input())
line_dict = {}
for row in graph:
    line_dict[row] = line_dict.get(row, 0) + 1
line_dict = list(line_dict.items())
line_dict.sort(key = lambda x : -x[1])

answer = 0
for t, n in line_dict:
    # 0의 개수가 스위치를 누르는 횟수인 K보다 많으면 
    # 절대로 꺼져있는 램프들을 다 못 킴
    zero_cnt = t.count('0')
    if K >= zero_cnt and K % 2 == zero_cnt % 2:
        answer = n
        break
print(answer)