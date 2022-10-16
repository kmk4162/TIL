T = int(input())

for testcase in range(T):
    result = 0
    s = int(input())
    for i in range(int(input())):
        p, q = map(int, input().split())
        result += p * q
    print(result + s)

