start, end = map(int, input().split())
list1 = []

def seq(a):
    for i in range(1, a + 1):
        for j in range(i):
            list1.append(i)
    return list1
seq(50)
x = sum(list1[start - 1 : end])
# 실제 순서는 1 2 3 4 ...지만
# 파이썬의 index는 0 1 2 3 4기 때문에
# start -1 처리, end는 어차피 미만까지니까 그대로
print(x)