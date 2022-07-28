# 모형 1개당 S 2개 A 2개 필요
M, N = map(int, input().split())
cnt = 0

S_max = M // 2
A_max = N // 2
# M이 100 N이 15라면 S_max는 50, A_max는 7
print(min(S_max, A_max))
