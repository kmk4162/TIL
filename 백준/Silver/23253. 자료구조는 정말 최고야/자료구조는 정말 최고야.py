from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
# 스택 수(M)만큼 입력 받기
stacklist = deque()

for i in range(1, M + 1):
    book_count = int(input())
    book_numbers = list(map(int, input().split()))
    stacklist.append(book_numbers)

for i in stacklist:
    if i != sorted(i, reverse = True):
        print('No')
        break
else:
    print('Yes')

# 순서대로 책을 꺼내려면 모든 스택이 내림차순으로 정렬돼있어야함
# 따라서 순서대로 책 꺼내기가 가능하다면 sort로 정렬해도 기존 순서랑
# 동일해야 하지만, 만약 순서가 바뀐다면 애초부터 내림차순 정렬이 아니였다는
# 뜻이기 때문에 순서대로 책을 꺼내기가 불가능함

#* 스택 사용법

# 맨 위(top)위치의 값을 pop()하고 그전의 인덱스의 값과
# 계속 비교하는 방식

for stack in stacklist:
    comparison = stack.pop()
    answer = 'Yes' # 미리 Yes를 디폴트로 정해둠

    while len(stack) != 0:
        if stack[-1] > comparison: 
            comparison = stack.pop()  
        else:
            answer = 'No'
            break
print(answer)


