def solution(nums):
    N = len(nums) // 2
    ponketmon = {}
    for i in nums:
        ponketmon[i] = ponketmon.get(i, 0) + 1
    if N < len(ponketmon):
        return N
    else:
        return len(ponketmon)
    