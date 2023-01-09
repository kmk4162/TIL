import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
cnt = 0
block_size = 2 ** N # 한 변의 길이

def check(x, y, B):
    global cnt
    if x > r or x + B <= r or y > c or y + B <= c:
        cnt += B ** 2
        return

    if B > 2:
        check(x, y, B // 2) 
        check(x, y + B // 2, B // 2) 
        check(x + B // 2, y, B // 2) 
        check(x + B // 2, y + B // 2, B // 2)
    else:
        if x == r and y == c:
            print(cnt)
        elif x == r and y + 1 == c:
            print(cnt + 1)
        elif x + 1 == r and y == c:
            print(cnt + 2)
        else:
            print(cnt + 3)

check(0, 0, block_size)