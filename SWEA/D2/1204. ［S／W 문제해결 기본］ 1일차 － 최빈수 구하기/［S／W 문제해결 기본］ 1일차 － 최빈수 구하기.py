T = int(input())

for test_case in range(T):
    case_num = int(input())
    scores = list(map(int, input().split()))
    score_dict = {}
    # 1번에 천개씩 들어옴
    for i in scores:
        score_dict[i] = score_dict.get(i, 0) + 1
    x = sorted(score_dict.items(), key = lambda x : -x[1])
    # items는 key,value 순서이고 value 기준 내림차순으로 정렬하면
    # 가장 큰 value가 처음으로 정렬됨
    result = x[0][0]
    print(f'#{case_num} {result}')