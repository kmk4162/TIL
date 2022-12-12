import sys
input = sys.stdin.readline

arr = set(i for i in range(1, 31))
arr1 = []
for i in range(28):
    arr1.append(int(input()))
result = arr - set(arr1)
print(min(result))
print(max(result))