fbi = []
for i in range(1, 6):
    name = input()
    if 'FBI' in name:
        fbi.append(i)
if fbi:
    print(*fbi)
else:
    print('HE GOT AWAY!')