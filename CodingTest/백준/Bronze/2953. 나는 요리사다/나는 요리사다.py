scores_list = []
for i in range(5):
    score = list(map(int, input().split()))
    scores_list.append(sum(score))
# 한 줄씩 입력 받고 더한 값을 리스트에 하나씩 저장
#* scores_list에 [14, 17, 16, 16, 16] 이런식으로 저장

winner = scores_list[0]
winner_cnt = 1
for i in range(1, len(scores_list)):
    if scores_list[i] > winner:
        winner = scores_list[i]
        winner_cnt = i + 1
        # 두번째 사람이 우승자라면 winner_cnt는 2여야하고
        # i는 1이기때문에 i + 1이 winner_cnt가 됨
    else:
        continue
print(winner_cnt, winner)

