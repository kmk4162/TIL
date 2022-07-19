A = int(input())
B = int(input())
C = int(input())
result = A * B * C
r_list = str(result)
#* 문자열로 변환 후 list를 하면 자리 하나하나 별로 요소가 나뉘어짐!
num_dict = {}

for i in r_list:
    num_dict[int(i)] = num_dict.get(int(i), 0) + 1
#* 딕셔너리에 횟수 저장
for j in range(0, 10):
    print(num_dict.get(j , 0))