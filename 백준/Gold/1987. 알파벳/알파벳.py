import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for i in range(R):
    line = list(input().strip())
    graph.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(x, y, word_dict, cnt):
    global answer
    answer = max(answer, cnt)
    
    for d in range(4):
        new_x = x + dx[d]
        new_y = y + dy[d]
        if -1 < new_x < R and -1 < new_y < C and not graph[new_x][new_y] in word_dict:
            word_dict.add(graph[new_x][new_y])
            check(new_x, new_y, word_dict, cnt + 1)
    word_dict.remove(graph[x][y])

answer = 0
word_dict = set()
word_dict.add(graph[0][0])
check(0, 0, word_dict, 1)
print(answer)