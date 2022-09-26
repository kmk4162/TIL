import sys
input = sys.stdin.readline

# 1의 자리가 무엇인지 판단하기
T = int(input())
for i in range(T):
    answer = 0
    cycle = []
    a, b = input().split()

    if a[-1] == '1':
        cycle = [1]
    elif a[-1] == '2':
        cycle = [2, 4, 8, 6]
    elif a[-1] == '3':
        cycle = [3, 9, 7, 1]
    elif a[-1] == '4':
        cycle = [4, 6]
    elif a[-1] == '5':
        cycle = [5]
    elif a[-1] == '6':
        cycle = [6]
    elif a[-1] == '7':
        cycle = [7, 9, 3, 1]
    elif a[-1] == '8':
        cycle = [8, 4, 2, 6]
    elif a[-1] == '9':
        cycle = [9, 1]
    elif a[-1] == '0':
        cycle = [10]
    idx = int(b) % len(cycle)
    print(cycle[idx - 1])