import sys
input = sys.stdin.readline

list = ['a','b','k','d','e','g','h','i','l','m','n','ng','o','p','r','s','t','u','w','y']
numlist = []
for case in range(int(input())):
    word = input().rstrip()
    ans = []
    for char in range(len(word)):
        if word[char] != 'n':
            x = list.index(word[char])
            ans.append(x)
        else:
            if char == len(word) - 1:
                ans.append(10)
            else:
                if word[char + 1] == 'g':
                    ans.append(11)
                else:
                    ans.append(10)
    numlist.append((ans, word))
numlist.sort(key = lambda x: x[0])

for i in numlist:
    print(i[1])