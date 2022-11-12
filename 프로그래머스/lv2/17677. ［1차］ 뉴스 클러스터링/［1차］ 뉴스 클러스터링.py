def solution(str1, str2):
    # 영문만 유효 -> 아스키코드로 구별, 97 ~ 122
    str1 = str1.lower()
    str2 = str2.lower()
    # 2개씩 끊은 부분 문자열 담을 리스트
    str1_list = []
    str2_list = []
    # 영어로만 이루어진 부분 문자열만 추가
    for i in range(len(str1) - 1):
        if 97 <= ord(str1[i]) <= 122 and 97 <= ord(str1[i+1]) <= 122:
            word = str1[i : i + 2]
            str1_list.append(word)
    for i in range(len(str2) - 1):
        if 97 <= ord(str2[i]) <= 122 and 97 <= ord(str2[i+1]) <= 122:
            word = str2[i : i + 2]
            str2_list.append(word)
    # 2번 조작해야 하니까 똑같이 만들기
    copy_str1_list = str1_list.copy()
    copy_str2_list = str2_list.copy()
    
    # 다중 합집합 구하기
    sum_list = []
    for word in str1_list:
        if word in str2_list:
            sum_list.append(word)
            str2_list.remove(word)
        else:
            sum_list.append(word)
    # 나머지도 합집합 리스트에 넣어주기
    for i in str2_list:
        sum_list.append(i)
    
    # 다중 교집합 구하기
    same_list = []
    for word in copy_str1_list:
        if word in copy_str2_list:
            same_list.append(word)
            copy_str2_list.remove(word)
    print(sum_list)
    print(same_list)
    # 예외 처리
    if len(same_list) == 0 and len(sum_list) == 0:
        result = 1
    else:
        result = len(same_list) / len(sum_list)
    return int(result * 65536)
            
            