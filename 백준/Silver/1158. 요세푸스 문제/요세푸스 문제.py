import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
num_list = list(range(1, N + 1))
num_list = deque(num_list)
answer = []

while num_list:
    # 맨 앞의 수를 팝하고 다시 뒤로 넣는 과정을 K - 1번 반복하고
    # K번째로 돌아오는 수는 num_list에서 제거하고 answer에 넣기
    for i in range(K - 1):
        x = num_list.popleft()
        num_list.append(x)
    answer.append(num_list.popleft())
print(str(answer).replace('[','<').replace(']','>'))