import sys
input = sys.stdin.readline

N = int(input())
list = []
counts = {}
for _ in range(N):
    num = int(input())
    list.append(num)
    counts[num] = counts.get(num, 0) + 1

avg = sum(list) / len(list)
print(round(avg))

sorted_list = sorted(list)
print(sorted_list[(len(list) - 1) // 2])

new_counts = sorted(counts.items(), key = lambda x : (-x[1], x[0]))
ans = new_counts[0][1]

if len(new_counts) == 1:
    print(new_counts[0][0])
else:
    if new_counts[1][1] < ans:
        print(new_counts[0][0])
    else:
        print(new_counts[1][0])
print(max(list) - min(list))