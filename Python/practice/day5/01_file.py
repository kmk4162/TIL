# 'r' : read(일기 전용)
# 'w' : write(쓰기 전용 - 덮어씀)
# 'a' : write(이어쓰기)

with open('test.txt', 'w', encoding = 'utf-8') as f:
    f.write('Hello world!\n')
    for i in range(1, 6):
        f.write(f'{i} 번째\n')