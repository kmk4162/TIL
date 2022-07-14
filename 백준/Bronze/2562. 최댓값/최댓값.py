num_list = []
for i in range(9) :
    num_list.append(int(input()))  			## num_lst 안에 입력된 값들 차례대로 넣기

print(max(num_list))						## max라는 메소드를 이용해 num_lst 내의 최댓값 출력하기
print(num_list.index(max(num_list))+1)