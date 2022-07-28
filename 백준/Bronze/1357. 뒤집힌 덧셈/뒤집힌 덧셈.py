X, Y = map(str, input().split())

def Rev(a):
    rev_a = a[::-1]
    return rev_a


A = str(int(Rev(X)) + int(Rev(Y)))
print(int(Rev(A)))