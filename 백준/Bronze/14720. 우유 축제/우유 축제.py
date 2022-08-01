# 딸기 0, 초코 1, 바나나 2
# 먹는 순서는 항상 0 1 2 0 1 2 ...
from collections import deque

num = int(input())
milks = deque(input().split())
drunk_list = []
cnt = 0

while len(milks) > 0:
    if milks[0] == str(cnt):
        x = milks.popleft()
        drunk_list.append(x)
        cnt += 1
    else:
        milks.popleft()
    if cnt == 3:
        cnt = 0
    
print(len(drunk_list))

# 일단 맨 왼쪽을 항상 popleft하는데 0이면 cnt가 올라감
# 0이 아니면 그냥 popleft만 함
# 0이 1번 존재했다면 1이 있을때 cnt가 올라감
# 항상 리스트의 맨 왼쪽이 상황별로 (0 or 1 or 2)일 때 
# drunk_list에 popleft한 요소를 append해줌
# 0 1 2가 순서대로 나와서 cnt가 3이되면 다시 0으로 초기화
