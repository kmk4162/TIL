T = int(input())

for _ in range(T):
    # k는 층, n은 호실
    k = int(input())
    n = int(input())
    # k는 3, n은 5라고 가정

    # 0층
    line = [i for i in range(1, n + 1)]
    
    floor = 0
    while True:
        for room in range(1, n):
            line[room] += line[room - 1]
        floor += 1
        if floor == k:  
            result = line[-1]
            break
    print(result)