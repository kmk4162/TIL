for i in range(int(input())):
    a_dict = {}
    b_dict = {}
    # a_dict와 b_dict가 같으면 애너그램이됨
    a, b = input().split()
    for char in a:
        a_dict[char] = a_dict.get(char, 0) + 1
    for char in b:
        b_dict[char] = b_dict.get(char, 0) + 1

    if a_dict == b_dict:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')