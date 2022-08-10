N = int(input())
cow = {}
cnt = 0
for i in range(N):
    cow_number, location = map(int, input().split())
    # 소의 번호가 있으면 추가받으면서 location이 같은지 다른지 체크
    if cow_number in cow:
        # 위치가 다르면 카운트도 올려주면서 위치도 업데이트
        # 위치가 같으면 그대로 넘어감
        if location != cow[cow_number]:
            cow[cow_number] = location
            cnt += 1
    # 소의 번호가 없으면 새로 추가, 카운트는 변화 없음
    else:
        cow[cow_number] = location
print(cnt)