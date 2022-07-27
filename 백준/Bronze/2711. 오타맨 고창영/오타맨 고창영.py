# T = int(input())

# for test_case in (1, T + 1):
#     index, miss = input().split()
#     for i in range(len(miss)):
#         if i + 1 == int(index):
#             new = miss.replace(miss[i],'')
#             break
#     print(new)
#! replace 함수를 이용하면 인덱스 값을 지정해서 삭제할 수 없다!
#! 따라서 잘못된 접근 방법!

# 찾은 풀이
#* 1. 문자열 슬라이싱
T = int(input())

for i in range(T):
    n, word = input().split()
    n = int(n)
    print(word[:n-1] + word[n:])

#* 2. pop 쓰기
# T = int(input())
# for i in range(T):
#     i, word = input().split()
#     i = int(i)
#     word = list(word)
#     word.pop(i-1)
#     print(''.join(word))

