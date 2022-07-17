# 문자열 word의 길이를 출력하는 코드
#! len() 함수 사용 금지

word = input()
cnt = 0

# 1. while문

while(word != ""):
    cnt+=1
    word = word[1:]
print(cnt)

# 2-1. for문: 문자열 그대로 사용

for i in word:
    cnt += 1
print(f'길이는 {cnt} 입니다')

# 2-2. for문: index 사용

for i in range(len(word)):
    cnt += 1
    print()
print(f'길이는 {cnt} 입니다')