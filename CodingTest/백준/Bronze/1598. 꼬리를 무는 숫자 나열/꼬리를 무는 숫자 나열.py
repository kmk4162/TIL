a, b = map(int, input().split())

row_distance = abs(((a - 1) // 4) - ((b - 1) // 4))
col_distance = abs(((a - 1) % 4) - ((b - 1) % 4))
print(row_distance + col_distance)