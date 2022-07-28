# 숫자 1은 2초, ABC는 3초, DEF는 4초 ... TUV는 9초, WXYZ는 10초
# UNUCIC는 868242 -> 다이얼 사진에 영어 적혀있음
# 각 영어마다 적혀있는 숫자 + 1을 해줘야함

num_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS',
'TUV', 'WXYYZ']

word = input()
cnt = 0

for i in word:
    for j in range(len(num_list)):
        if i in num_list[j]:
            cnt += (j + 3)
print(cnt)

