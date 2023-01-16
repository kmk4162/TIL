import sys
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

cnt_a = 0
cnt_b = 0
cnt_c = 0
def check(row, col, B):
    global cnt_a, cnt_b, cnt_c
    x, y, z = 0, 0, 0 # -1, 0, 1
    for i in range(row, row + B):
        for j in range(col, col + B):
            if graph[i][j] == -1:
                x += 1
            elif graph[i][j] == 0:
                y += 1
            else:
                z += 1
    if x == B ** 2:
        cnt_a += 1
        return
    elif y == B ** 2:
        cnt_b += 1
        return
    elif z == B ** 2:
        cnt_c += 1
        return
    else:
        b = B // 3
        check(row, col, b)
        check(row + b, col, b)
        check(row + 2*b, col, b)
        check(row, col + b, b)
        check(row + b, col + b, b)
        check(row + 2*b, col + b, b)
        check(row, col + 2*b, b)
        check(row + b, col + 2*b, b)
        check(row + 2*b, col + 2*b, b)
check(0, 0, N)
print(cnt_a)
print(cnt_b)
print(cnt_c)