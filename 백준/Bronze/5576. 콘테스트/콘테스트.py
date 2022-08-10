# 리스트에 입력 받기
list_W = []
list_K = []
for _ in range(10):
    list_W.append(int(input()))
for _ in range(10):
    list_K.append(int(input()))
    
# 정렬하고 3번째까지의 합만 구하기 
list_W.sort(reverse = True)
list_K.sort(reverse = True)
print(sum(list_W[:3]), sum(list_K[:3]))