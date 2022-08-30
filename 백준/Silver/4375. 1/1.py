while True:
    cnt = '1'
    try:
        A = int(input())
    except EOFError:
        break
    if A == 1:
        print(1)
        break
    while True:
        cnt += '1'
        if int(cnt) % A == 0:
            print(len(cnt))
            break