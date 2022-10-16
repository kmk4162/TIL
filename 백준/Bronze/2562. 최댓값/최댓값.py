big_cnt = 0
big = 0

for i in range(9):
    num = int(input())
    if big < num:
        big = num
        big_cnt = i
    
print(big)
print(big_cnt + 1)