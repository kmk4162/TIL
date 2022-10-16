import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(T):
    num = int(input())
    grade = []
    for i in range(num):
        paper, interview = map(int, input().split())
        grade.append((paper, interview))
    grade.sort(key = lambda x : (x[0], x[1]))
    comp = grade[0]
    cnt = 0
    for j in range(len(grade)):
        if grade[j][0] > comp[0] and grade[j][1] > comp[1]:
            continue
        else:
            cnt += 1
            comp = grade[j]
    print(cnt)