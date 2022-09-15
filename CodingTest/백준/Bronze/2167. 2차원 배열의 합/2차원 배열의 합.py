import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = []
for _ in range(N):
    x = list(map(int, input().split()))
    num_list.append(x)

test_case = int(input())
for i in range(test_case):
    result = 0
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1
    for row in range(i, x + 1):
        for col in range(j, y + 1):
            result += num_list[row][col]
    print(result)