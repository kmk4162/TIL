word = input()
# 왼쪽 오른쪽을 얼굴 기준으로 나누자

#* 왼쪽, 오른쪽 나누기
left, right = map(str, word.split('(^0^)'))

# 왼쪽 오른쪽 잔상 카운트
lcnt = 0
rcnt = 0
for i in left:
    if i == '@':
        lcnt += 1   
for i in right:
    if i == '@':
        rcnt += 1
print(lcnt, rcnt)   