N = int(input())
cnt = 3
result = 0
while True:
    cnt += 1
    fourseven = True
    for char in str(cnt):
        if char == '4' or char == '7':
            continue
        else:
            fourseven = False
            break
    if fourseven == True:
        result = cnt
    if cnt == N:
        print(result)
        break
