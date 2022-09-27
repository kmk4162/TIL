import sys
input = sys.stdin.readline

N, P, Q = map(int, input().split())

numdict = {0 : 1}

def find_number(idx):
    global numdict
    # 이미 사전에 idx값이 있는 경우는 바로 return해주면 됨
    if numdict.get(idx):
        return numdict[idx]
    newidx1 = idx // P
    newidx2 = idx // Q
    numdict[idx] = find_number(newidx1) + find_number(newidx2)
    return numdict[idx]

find_number(N)
print(numdict[N])