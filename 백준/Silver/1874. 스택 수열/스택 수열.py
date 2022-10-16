import sys
input = sys.stdin.readline

# 입력 순서대로 pop을 해야함
N = int(input())
Nlist = []
for i in range(N):
    Nlist.append(int(input()))
# [4, 3, 6, 8, 7, 5, 2, 1]

stack = []
idx = 0
num = 0
answer = ''
cnt = 0
mystack = []
while True:
    if not stack or stack[-1] < Nlist[idx]:
        num += 1
        stack.append(num)
        answer += '+'  
    # 같다면 pop을 해줘야함
    else:
        x = stack.pop()
        # if x != Nlist[idx]:
        #     break
        idx += 1
        answer += '-'
        mystack.append(x)
        cnt += 1
        # print(mystack)
    if cnt == N:
        break
if mystack == Nlist:
    for i in answer:
        print(i)
else:
    print('NO')