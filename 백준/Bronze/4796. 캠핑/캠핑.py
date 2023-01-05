cnt = 0
while True:
    cnt += 1
    L, P, V = map(int, input().split())
    if (L, P, V) == (0, 0, 0):
        break
    answer = (V // P) * L
    if (V % P) > L:
        answer += L
    else:
        answer += (V % P) 
    print(f'Case {cnt}: {answer}')