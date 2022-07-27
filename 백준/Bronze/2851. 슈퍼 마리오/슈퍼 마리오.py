score = 0
score_list = []
overlist = []
underlist = []

for i in range(10):
    score += int(input())
    score_list.append(score)
# 점수 리스트 완성

for i in score_list:
    if i < 100:
        underlist.append(i)
    else:
        overlist.append(i)
# 100미만과 100이상 점수들을 가르고 
# underlist의 제일 큰 수와 overlist의 제일 작은 수를 비교
if len(underlist) == 0:
    underscore = 0
else:
    underscore = underlist[-1]

if len(overlist) == 0:
    overscore = 0
else:
    overscore = overlist[0]
# 모든 score가 100이 넘지 않으면 overlist에 아무것도 없음
# overlist의 길이가 0이 되기 때문에 인덱싱 오류가 발생
# 길이가 0인 경우에만 overscore = 0으로 둠
# score가 처음부터 100이 들어오게 되면 underlist에 아무것도 없는 경우도 생김
# 길이가 역시 0인 경우에만 underscore = 0

if overscore == 0:
    print(underscore)
elif underscore == 0:
    print(overscore)
elif 100 - underscore >= overscore - 100:
    print(overscore)
else:
    print(underscore)


