S = input()
list = []
for i in range(len(S)):
    answer = S[i:]
    list.append(answer)
list.sort()
for li in list:
    print(li)