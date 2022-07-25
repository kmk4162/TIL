A = int(input())
B = int(input())
C = int(input())
result = str(A * B * C)
num_list = [0] * 10
for num in result:
    num_list[int(num)] += 1
for i in num_list:
    print(i)