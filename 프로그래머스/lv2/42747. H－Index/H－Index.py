def solution(citations):
    citations.sort(reverse = True)
    print(citations)
    h = 0
    while True:
        cnt = 0
        for i in citations:
            if i >= h:
                cnt += 1
            else:
                break
        if cnt >= h:
            h += 1
            continue
        else:
            break
    return h - 1
                
            
    