for test_case in range(10):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    # 1 기본괄호, 2 대괄호 3 중괄호 4 꺽쇠
    num = int(input())
    word = input()
    for char in word:
        if char == '(':
            cnt1 += 1
        elif char == ')':
            cnt1 -= 1
        elif char == '[':
            cnt2 += 1
        elif char == ']':
            cnt2 -= 1
        elif char == '{':
            cnt3 += 1
        elif char == '}':
            cnt3 -= 1
        elif char == '<':
            cnt4 += 1
        else:
            cnt4 -= 1
    if cnt1 == 0 and cnt2 == 0 and cnt3 == 0 and cnt4 == 0:
        result = 1
    else:
        result = 0
    print(f'#{test_case + 1}', result)