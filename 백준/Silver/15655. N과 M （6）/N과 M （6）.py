n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
s = []

def nm():
    if len(s) == m:
        if s == sorted(s):
            print(' '.join(map(str, s)))
        return
    for i in nums:
        if i in s:
            continue
        s.append(i)
        nm()
        s.pop()

nm()