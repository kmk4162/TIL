class MyClass:
    class_variable = '클래스 변수'

    #* 메서드를 정의
    def __init__(self):
        self.instance_varibale = '인스턴스 변수'
    #* 인스턴스 메서드 정의
    def instance_method(self):
        return self, self.instance_variable
    #* 클래스 메서드 정의
    @classmethod
    def class_method(cls):
        return cls, cls.class_variable
    #* 스태틱 메서드 정의
    @staticmethod
    def static_method():
        return ''

c1 = MyClass()
print('인스턴스 변수 호출', c1.instance_varibale)
print('인스턴스 메서드 호출', c1.instance_method())
print('클래스 메서드 호출', c1.class_method())
print('스태틱 메서드 호출', c1.static_method())