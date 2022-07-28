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