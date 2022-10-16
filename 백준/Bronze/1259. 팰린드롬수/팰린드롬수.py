import sys

input = sys.stdin.readline

while True:
    temp = input().rstrip()
    if temp != '0':
        if temp == temp[::-1]:
            print('yes')
        else:
            print('no')
    else:
        break