N = int(input())
N_numbers = list(map(int, input().split()))

M = int(input())
M_numbers = list(map(int, input().split()))

# ----------------------------------------------------------------
count_dict = {}
for i in N_numbers:
    count_dict[i] = count_dict.get(i, 0) + 1

for i in M_numbers:
    if i in count_dict:
        print(count_dict[i], end = ' ')
    else:
        print(0, end = ' ')
