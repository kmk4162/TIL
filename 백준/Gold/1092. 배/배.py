import sys
input = sys.stdin.readline

N = int(input())
machine = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))
machine.sort(reverse = True)
box.sort(reverse = True)
cnt = 0
if machine[0] < box[0]:
    cnt = -1
else:
    while True:
        cnt += 1
        for i in range(len(machine)):
            for j in range(len(box)):
                if machine[i] >= box[j]:
                    box.pop(j)
                    break
        if len(box) == 0:
            break
print(cnt)