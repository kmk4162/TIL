import sys
input = sys.stdin.readline

n = int(input())
n_dict = {}
for i in range(n):
    cnt = int(input())
    n_dict[cnt] = n_dict.get(cnt, 0 ) + 1
n_dict = sorted(n_dict.items(), key = lambda x: (-x[1], x[0]))
print(n_dict[0][0])