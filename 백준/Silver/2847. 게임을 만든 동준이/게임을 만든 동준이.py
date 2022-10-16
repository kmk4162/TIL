import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

cnt = 0
for i in range(len(numbers)-2, -1,  -1):
    if numbers[i] >= numbers[i + 1] -1:
        temp = numbers[i]
        numbers[i] = numbers[i + 1] - 1
        
        cnt += (temp - numbers[i])
print(cnt)