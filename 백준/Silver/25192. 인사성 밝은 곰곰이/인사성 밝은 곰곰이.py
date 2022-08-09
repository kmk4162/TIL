N = int(input())
ndict = {}
gomgom = 0
for i in range(N):
    name = input()
    if name == 'ENTER':
        ndict = {}
        continue
    else:
        if name not in ndict:
            gomgom += 1
        ndict[name] = ndict.get(name, 0) + 1
print(gomgom)
