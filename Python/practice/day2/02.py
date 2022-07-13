# 문자열 word의 길이를 출력하는 코드를 
# 1) while문 2) for문(문자열 그대로) 3) for문(index)으로 각각 작성하시오.
# len() 함수 사용 금지

# while문
cnt = 0
while(word != ""):
    cnt+=1
    word = word[1:]
print(cnt)

# for문
cnt = 0
for i in word:
    cnt += 1
    print(cnt)
print(f'길이는 {cnt} 입니다')