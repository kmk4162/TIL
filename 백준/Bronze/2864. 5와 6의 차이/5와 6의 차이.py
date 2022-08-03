A, B = input().split()
# 최소는 5는 그대로 6은 무조건 5로 바꾸고
# 최대는 5는 6으로 바꾸고 6은 그대로 두기

#* 최솟값 구하기; 6을 5로 바꾸기
def low(x, y):
    for i in x:
        if '6' in x:
            x = x.replace('6', '5')
    for i in y:
        if '6' in y:
            y = y.replace('6', '5')
    return int(x) + int(y)

#* 최댓값 구하기; 5를 6으로 바꾸기
def high(x, y):
    for i in x:
        if '5' in x:
            x = x.replace('5', '6')
    for i in y:
        if '5' in y:
            y = y.replace('5', '6')
    return int(x) + int(y)
print(low(A, B), high(A, B))
