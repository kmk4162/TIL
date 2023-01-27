import sys
input = sys.stdin.readline

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
moeum = ['a', 'e', 'i', 'o', 'u']
order_dict = {}
for i in range(C):
    order_dict[arr[i]] = i
# print(order_dict)

answer = []
moeum_cnt = 0
jaeum_cnt = 0
def dfs():
    global moeum_cnt, jaeum_cnt
    if len(answer) == L:
        if moeum_cnt >= 1 and jaeum_cnt >= 2:
            print(''.join(answer))
        return
    
    for i in range(C):
        if len(answer) == 0:
            if arr[i] in moeum:
                moeum_cnt += 1
            else:
                jaeum_cnt += 1
            answer.append(arr[i])
            dfs()
            if answer.pop() in moeum:
                moeum_cnt -= 1
            else:
                jaeum_cnt -= 1
        else:
            if arr[i] not in answer and order_dict[answer[-1]] < order_dict[arr[i]]:
                if arr[i] in moeum:
                    moeum_cnt += 1
                else:
                    jaeum_cnt += 1
                answer.append(arr[i])
                dfs()
                if answer.pop() in moeum:
                    moeum_cnt -= 1
                else:
                    jaeum_cnt -= 1
dfs()