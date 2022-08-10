a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == 60 and b == 60 and c == 60:
        print('Equilateral')
    elif a ==b or b == c or c == a:
        print('Isosceles')
    elif a != b and a != c and b != c:
        print('Scalene')
else:
    print('Error')