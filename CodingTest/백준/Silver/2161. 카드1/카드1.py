from collections import deque

T = int(input())
queue = deque(range(1, T + 1))
result = []
while len(queue) > 1:
    x = queue.popleft()
    print(x, end = ' ')
    result.append(x)
    y = queue.popleft()
    queue.append(y)
print(queue[0])
    

