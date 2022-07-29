from cmath import log


N = int(input())

log_dict = {
}
# 입력 받고 딕셔너리 형성
for i in range(N):
    key, value = input().split()
    log_dict[key] = value

enter_list = []
for key in log_dict:
    if log_dict[key] == 'enter':
        enter_list.append(key)
enter_list.sort(reverse=True)
# 이름 정렬
for name in enter_list:
    print(name)
