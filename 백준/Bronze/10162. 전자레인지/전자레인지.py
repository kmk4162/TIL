import sys
input = sys.stdin.readline

T = int(input())
times = [300, 60, 10]
times_cnt = [0, 0, 0]
for time in range(len(times)):
    if T // times[time] > 0:
        cnt = T // times[time]
        T -= cnt * times[time]
        times_cnt[time] += cnt
if T != 0:
    print(-1)
else:
    print(*times_cnt)