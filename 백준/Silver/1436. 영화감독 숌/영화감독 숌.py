import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
number = 665

while True:
    number += 1
    if '666' in str(number):
        cnt += 1
    if cnt == N:
        break
print(number)