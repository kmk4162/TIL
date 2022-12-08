import sys
input = sys.stdin.readline

N = int(input())
paper = []
for i in range(N):
    line = list(map(int, input().split()))
    paper.append(line)
# 하얀색이 0, 파란색이 1
white_cnt = 0
blue_cnt = 0

def func(graph):
    # 입력값 자체가 전부 하얗거나 파란색이면 제외
    N = len(graph)
    first_cnt = 0
    global white_cnt, blue_cnt
    for i in range(N):
        for j in range(N):
            first_cnt += graph[i][j]
    if first_cnt == 0:
        white_cnt = 1
        return
    elif first_cnt == N ** 2:
        blue_cnt = 1
        return
    splited_papers = []
    paper1 = []
    paper2 = []
    paper3 = []
    paper4 = []
    for a in range(0, N//2):
        line = graph[a][0 : N//2]
        paper1.append(line)
    for b in range(0, N//2):
        line = graph[b][N//2 : N]
        paper2.append(line)
    for c in range(N//2, N):
        line = graph[c][0 : N//2]
        paper3.append(line)
    for d in range(N//2, N):
        line = graph[d][N//2 : N]
        paper4.append(line)
    splited_papers.append(paper1)
    splited_papers.append(paper2)
    splited_papers.append(paper3)
    splited_papers.append(paper4)

    # 전체 칸의 합이 0 아니면 (N//2) ** 2가 아니면 나눠야함
    # 전체 색이 같은지 판별
    for graph in splited_papers:
        cnt = 0
        for line in graph:
            cnt += sum(line)
        # 전부 하얀색
        if cnt == 0:
            white_cnt += 1
        elif cnt == (N // 2) ** 2:
            blue_cnt += 1
        else:
            func(graph)

func(paper)
print(white_cnt)
print(blue_cnt)