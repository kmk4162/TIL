# 파일명, 어떤 모드로 열지, 인코딩 설정
# 원래는 open후 close해야하는데 with를 쓰면 코드블럭 실행 완료되면
# 자동으로 close됨! -> 그러니 with를 쓰자!

with open('student.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    #text는 string 타입
    names = text.split()
    # string.split() -> list 타입
    cnt = 0
    for i in names:
        if i[0] == '김':
            # if name.startswith('김')도 가능!
            cnt +=1
    print(cnt)