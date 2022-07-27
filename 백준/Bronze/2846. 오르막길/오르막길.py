# N = int(input())

# height_list = list(map(int, input().split()))
# start_pos = height_list[0]
# height_diffs = []
# height_diff = 0

# for i in height_list:
#     if i > start_pos:
#         height_diff += (i - start_pos)
#         height_diffs.append(height_diff)
#         start_pos = i
#     else:
#         height_diff = 0
#         start_pos = i
# if bool(height_diffs) is True:   
#     print(sorted(height_diffs)[-1])
# else:
#     print(0)
# 입력받은 리스트의 요소들을 순회하면서 이전 숫자(높이)보다 큰 경우에만
# 그 차이를 height_diff에 저장하고 height_diffs 리스트에 저장
# 이전 높이보다 낮으면 바로 차이를 초기화 하고 리스트에 추가하지는 않음
# 오르막길이 여러개가 있다면 가장 큰 높이차를 출력해야하기 때문에
# sorted로 정렬한 다음 마지막 인덱스 값 출력
# 만약에 오르막길이 하나도 없었다면 height_diffs 리스트는 빈 리스트일 것이고
# 빈 리스트의 bool 값은 false이기 때문에
# if bool(height_diffs) is True 를 만족하지 못할 때는 0을 출력

#* 강사님 풀이법
N = int(input())
h_list = list(map(int, input().split()))
h_sum = 0 # 누적합 저장 변수
h_sum_list = [] # 누적합들 저장 리스트

for i in range(1, len(h_list)):
    if h_list[i] > h_list[i-1]:
        h_sum = h_sum + (h_list[i] - h_list[i-1])
        # 차이 누적합
        h_sum_list.append(h_sum)
    else:
        h_sum_list.append(h_sum)
        h_sum = 0
if len(h_sum_list) == 0:
    print(0)
print(max(h_sum_list))
# 가장 큰 차이만 출력


