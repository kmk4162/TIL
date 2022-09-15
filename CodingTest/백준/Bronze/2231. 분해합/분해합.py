N = int(input())
result = 1
gen_list = []
while result < N:
    digits = 0
    generator = 0
    for i in str(result):
        digits += int(i)
    generator = result + digits

    if generator == N:
        print(result)
        gen_list.append(result)
        break
    else:
        result += 1
        continue
if bool(gen_list) == False:
    print(0)

#* 검색해서 찾아본 코드
N = int(input())
result = 0

for i in range(1, N + 1):
    digits = list(map(int, str(i)))
    generator = sum(digits) + i
    if generator == N:
        result = i
        break
print(result)
# result값이 0이고 따로 업데이트 안 하면 그대로 0을 출력
# result값이 업데이트가 안 된다는 뜻은 조건에 맞는 generator가
# 없음을 의미하기 때문에 좀 더 깔끔하게 코드 작성 가능
