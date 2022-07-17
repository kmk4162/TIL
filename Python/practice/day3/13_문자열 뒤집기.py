# 주어진 문자열 word가 주어질 때
# 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

#* 1. 슬라이싱 스텝을 마이너스로 해서 풀기
#@ 가독성 측면에서는 나쁘지 않지만 메모리 사용량 측면에서는 안 좋음
#@ 같은 원소를 역방향으로 담고 있는 동일한 크기의 리스트를 새로 만들기 때문에
#@ 불필요하게 추가 메모리를 소모

word = input()
print(word[::-1])

#* 1-1. reversed() 내장함수랑 join 이용
#@ 역방향 루프시에는 다른 방법 대비해서 reversed()가 좋음
#@ 그리고 for문 이용해서 반복자를 반환하면 미리 메모리에 올려놓지 않고
#@ 필요할때마다 원소를 하나씩 제공하기 때문에 메모리 사용 측면에서 이점

word = input()
print(''.join(reversed(word)))

#* 1-2. 리스트의 reverse() 함수
#@ reverse()는 새로운 리스트를 생성하지 않고 기존 리스트의 원소들을 역방향으로 재배치
#@ reversed()는 반복자를 반환하고, reverse()는 단순히 리스트 내에 원소들이 제자리에서 역방향으로 배치
#@ reerse 메소드 자체의 반환 값은 없음고 원본을 바꾸어줌

word = input()
x = list(word)
x.reverse()
# 반환값 없이 자기자신을 변경
print(''.join(x))

#* 2. 문자열 더하는 순서를 바꿔주기
word = input()
new_word = ''

for i in word:
    new_word = i + new_word
    # i 뒤에 new_word를 붙여주는 것(순서가 매우 중요!!)
    # word가 apple이면
    # a
    # p + a
    # p + pa
    # l + ppa
    # e + lppa
    # elppa 이런식으로 동작하게 되는 것!
    print(new_word)
print(new_word)



