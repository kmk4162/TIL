import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for case in range(T):
    files_number, target_index = map(int, input().split())
    # 파일 개수 만큼 입력받기
    array = list(map(int, input().split()))
    # 각 문서마다 순서 인덱스를 같이 넣음
    files = []
    for i in range(len(array)):
        # 값, 인덱스 쌍
        elem = (array[i], i)
        files.append(elem)
    files = deque(files)
    # print(files)
    cnt = 0
    if files_number == 1:
        print(1)
        continue
    while files:
        now_file = files.popleft()
        # popleft 후 나머지 파일들의 가장 큰 중요도 구하기
        max_priority = 0
        for file in files:
            if file[0] > max_priority:
                max_priority = file[0]
        # 파일의 중요도가 나머지보다 크거나 같다면
        if now_file[0] >= max_priority:
            cnt += 1
            if now_file[1] == target_index:
                print(cnt)
                continue
        else:
            files.append(now_file)