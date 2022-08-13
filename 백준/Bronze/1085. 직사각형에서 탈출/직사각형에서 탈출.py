x, y, w, h = map(int, input().split())
minlist = list(map(abs, [x - 0, y - 0, x - w, y - h]))
print(min(minlist))