def solution(sizes):
    for i in sizes:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]
    row, col = 0, 0
    for i in sizes:
        if i[0] > row:
            row = i[0]
        if i[1] > col:
            col = i[1]
    return row * col
            
    