a, b = map(int, input().split())

div_list = []
div_cnt = 0
mul_cnt = 0

# a도 b도 나누었을때 나머지가 0인 애들만 리스트에 추가
while div_cnt < a or div_cnt < b:
    div_cnt += 1
    if a % div_cnt == 0 and b % div_cnt == 0:
        div_list.append(div_cnt)
gcd = div_list[-1]
# 어차피 1부터 작은 순서대로 비교 후 append하기 때문에
# 자연스럽게 div_list의 마지막 인덱스에는 최대공약수가 있음

lcm = int(a * b / gcd)
print(gcd)
print(lcm)

