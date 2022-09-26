import sys
input = sys.stdin.readline
from collections import deque

card_list = deque(range(1,int(input()) + 1))

while len(card_list) > 1:
    card_list.popleft()
    popcard = card_list.popleft()
    card_list.append(popcard)
    
print(card_list[0])