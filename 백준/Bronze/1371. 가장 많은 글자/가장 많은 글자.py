import sys

lines = []
count_dict = {}
# 임의의 줄 개수만큼 입력 받기
while True:
    try:
        line = input()
        lines.append(line)
    except:
        break
for line in lines:
    for char in line:
        count_dict[char] = count_dict.get(char, 0) + 1
# 공백도 문자열로 인식하니까 공백 키 제거
if ' ' in count_dict.keys():
    del(count_dict[' '])
# 많은 순서대로 내림차순 정렬, 영어 소문자 key는 오름차순으로 정렬
count_dict = dict(sorted(count_dict.items(), key = lambda x: (-x[1], x[0])))

# 나온 횟수가 공동이면 여러개 다 출력
large = max(count_dict.values())
for key, value in count_dict.items():
    if int(value) == large:
        print(key, end = '')



