T = int(input())

for test_case in range(1, T + 1):
    word = input()
    for i in range(1, 11):
        cnt = word[:i]
        cnt_next = word[i: 2 * i]
        if cnt == cnt_next:
            print(f'#{test_case}', i)
            break

