star = int(input())
star_string = '* ' # 뒤에 공백이 있는 문자열 단위를 생성
reverse_star_string = ' *'
for i in range(1, star + 1):
    if i % 2 == 1:
        print(star_string * star)
    else:
        print(reverse_star_string * star)
