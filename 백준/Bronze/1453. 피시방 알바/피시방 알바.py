number = int(input())
cnt = 0
numlist = list(map(int, input().split()))
print(len(numlist) - len(set(numlist)))


