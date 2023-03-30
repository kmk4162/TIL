import sys
input = sys.stdin.readline

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(T):
    cmd = input()
    x = 600
    y = 600
    d = 0 # 방향
    x_min, x_max, y_min, y_max = 600, 600, 600, 600
    locations = []
    locations.append((600, 600))
    for c in cmd:
        if c == 'F':
            x += dx[d]
            y += dy[d]
        elif c == 'B':
            x += dx[(d + 2) % 4]
            y += dy[(d + 2) % 4]
        elif c == 'R':
            d = (d + 1) % 4
        else:
            if d == 0:
                d = 3
            else:
                d -= 1
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x)
        y_max = max(y_max, y)
    print((x_max - x_min) * (y_max - y_min))