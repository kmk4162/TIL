from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    # 인덱스랑 값 쌍
    queue.append((0,0))
    while queue:
        idx, val = queue.popleft()
        if idx < len(numbers):
            queue.append((idx+1, val + numbers[idx]))
            queue.append((idx+1, val - numbers[idx]))
        else:
            if val == target:
                answer += 1
    return answer