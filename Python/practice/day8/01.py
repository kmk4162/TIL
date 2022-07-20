class Person:
    # 클래스 변수(속성)
    species = '사람'

    # 인스턴스 메서드
    # 인스턴스가 활용할 메서드
    def greeting(self):
        print('hi')

iu = Person()
# Person 클래스 안에 iu라는 인스턴스를 생성
iu.greeting()
#* 인스턴스를 생성하면 클래스 안에서 정의된 메서드를 사용할 수 있음!!

print(Person.species)