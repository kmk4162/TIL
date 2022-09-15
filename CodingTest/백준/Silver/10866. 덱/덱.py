import sys, math
input = sys.stdin.readline

from collections import deque

nums = deque()
for i in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'push_front':
        nums.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        nums.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if not nums:
            print(-1)
        else:
            x = nums.popleft()
            print(x)
    elif cmd[0] == 'pop_back':
        if not nums:
            print(-1)
        else:
            x = nums.pop()
            print(x)
    elif cmd[0] == 'size':
        print(len(nums))
    elif cmd[0] == 'empty':
        if not nums:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if nums:
            print(nums[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if nums:
            print(nums[-1])
        else:
            print(-1)