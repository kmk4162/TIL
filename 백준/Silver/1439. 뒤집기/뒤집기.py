S = input()
cnt = 1
now_char = S[0]
for char in S: 
    if char != now_char:
        now_char = char
        cnt += 1
print(cnt//2)