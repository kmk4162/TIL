import sys
input = sys.stdin.readline

N = int(input())
A = [0] * 46
B = [0] * 46

B[1] = 1
A[2] = 1
B[2] = 1
A[3] = 1
B[3] = 2
if N >= 4:
    for i in range(4, N + 1):
        A[i] = A[i - 1] + A[i - 2]
        B[i] = B[i - 1] + B[i - 2]
print(A[N], B[N])