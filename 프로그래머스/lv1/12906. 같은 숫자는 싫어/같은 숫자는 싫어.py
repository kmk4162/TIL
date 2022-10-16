def solution(arr):
    cur = 0
    before = arr[0]
    answer = []
    for num in range(1, len(arr)):
        cur = arr[num]
        if cur != before:
            answer.append(before)
            before = cur
    answer.append(cur)
    return answer