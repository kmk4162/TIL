import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)
    
# n = 1 -> 1
# n = 2 -> 2
# n = 3 -> 3
# n = 4 -> 5
# n = 5 -> 8

dp = [0 for _ in range(1001)]
n = int(input())
dp[1] = 1
dp[2] = 2

def tile(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    if dp[x] != 0:
        return dp[x]
    dp[x] = tile(x - 1) + tile(x - 2)
    return dp[x]

answer = tile(n) % 10007
print(answer)