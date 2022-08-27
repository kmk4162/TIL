def solution(new_id):
    #1
    result1 = new_id.lower()
    print(result1)
    
    #2
    list_2 = '~!@#$%^&*()=+[{]}:?,<>/'
    result2 = ''
    for char in range(len(result1)):
        if result1[char] not in list_2:
            result2 += result1[char]
    print(result2)
    
    #3
    cnt = 0
    temp = ''
    for char in range(len(result2)):
        if result2[char] == '.':
            cnt += 1
        else:
            if cnt >= 1:
                cnt = 0
                temp += '.'
                temp += result2[char]
            else:
                temp += result2[char]
    if cnt != 0:
        temp += '.'
    result3 = temp
    print(result3)
    
    #4
    # 변화가 없으면 그대로 사용
    temp = result3
    if result3[0] == '.':
        temp = result3[1:]
    if result3[-1] == '.':
        temp = temp[:-1]
    result4 = temp
    print(result4)
    
    #5
    if result4 == '':
        result5 = 'a'
    else:
        result5 = result4
    print(result5)
    
    #6
    result6 = 0
    if len(result5) >= 16:
        temp = result5[:15]
        if temp[-1] == '.':
            result6 = temp[:-1]
        else:
            result6 = temp
    else:
        result6 = result5
    print(result6)
    
    #7
    if len(result6) <= 2:
        # 문자열 길이
        x = len(result6)
        result7 = result6 + result6[-1] * (3 - x)
    else:
        result7 = result6
    print(result7)
    return result7
        
                