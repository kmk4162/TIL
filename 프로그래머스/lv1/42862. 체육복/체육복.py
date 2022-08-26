def solution(n, lost, reserve):
    students = [i for i in range(1, n + 1)]
    # lost = [2, 4] 가정
    lost.sort()
    reserve.sort()
    
    # 옷 리스트 만들기, 옷이 2인 사람만 빌려줄 수 있음
    shirts = [1] * n
    for i in reserve:
        shirts[i-1] += 1
    # 도난 당한 상황 고려
    for j in lost:
        shirts[j-1] -=1
    for i in range(len(shirts)):
        if shirts[i] == 0:
            if i == 0:
                pass
            else:
                if shirts[i-1] == 2:
                    shirts[i] += 1
                    shirts[i-1] -= 1
                    continue
            if i == n - 1:
                pass
            else:
                if shirts[i+1] == 2:
                    shirts[i] += 1
                    shirts[i+1] -= 1
                    continue
    print(shirts)
    noshirts = shirts.count(0)
    return n - noshirts
        