# 내 풀이
start, end = map(int, input().split())
list1 = []

def seq(a):
    for i in range(1, a + 1):
        for j in range(i):
            list1.append(i)
    return list1
seq(50)
x = sum(list1[start - 1 : end])
print(x)

# 실제 순서는 1 2 3 4 ...지만
# 파이썬의 index는 0 1 2 3 4기 때문에
# start -1 처리, end는 어차피 미만까지니까 그대로

#! -----------------------------------------------------------

#* 강사님 풀이 

# 수열의 길이가 B보다만 크면 됨(어차피 B가지의 합만 구하니까)
# 수열의 길이가 B보다 작을때 까지만 반복
#? 범위가 명확하면 for, 애매하면 while이 더 좋음 

# start, end = map(int, input().split())
# list1 = []
# N = 4

# while len(list1) < end:
#     for i in range(N):
#         list1.append(N)
#     N += 1

