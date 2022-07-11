A = int(input("")) #472
B = int(input("")) #385

a1 = int(A / 100)
a2 = int(A / 10 - a1 * 10)
a3 = int(A % 10)

b1 = int(B / 100)
b2 = int(B / 10 - b1 * 10)
b3 = int(B % 10)

print(A*b3)
print(A*b2)
print(A*b1)
print(A*B)



