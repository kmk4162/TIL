list_ = []
for i in range(9):
    list_.append(int(input()))
list_.sort()

# 키 합이 100이라 했으므로 9명 전체 합을 구한 뒤
# 2명의 합을 뺐을때 100이 되면 그 2명을 뺀 나머지가
# 진짜 일곱난쟁이들
total = sum(list_)
for i in range(8):
    for j in range(i + 1, 9):
        fakes = list_[i] + list_[j]
        if total - fakes  == 100:
            list_.remove(list_[j])
            list_.remove(list_[i])
            break
    # 추가 조건으로 이중 반복 멈추게 함
    # break 1개는 한번만 멈춤
    if len(list_) == 7:
        break
for i in list_:
    print(i)