import sys
input = sys.stdin.readline

N = int(input())
nums = []

for i in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        nums.append(cmd[1])
    elif cmd[0] == 'pop':
        if not nums:
            print(-1)
        else:
            x = nums.pop()
            print(x)
    elif cmd[0] == 'size':
        print(len(nums))
    elif cmd[0] == 'empty':
        if nums:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'top':
        if len(nums) != 0:
            print(nums[-1])
        else:
            print(-1)