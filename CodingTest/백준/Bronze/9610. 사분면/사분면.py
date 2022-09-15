n = int(input())
coord = {
    'Q1' : 0,
    'Q2' : 0,
    'Q3' : 0,
    'Q4' : 0,
    'AXIS' : 0
}
for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        coord['Q1'] = coord.get('Q1', 0) + 1
    elif x < 0 and y > 0:
        coord['Q2'] = coord.get('Q2', 0) + 1
    elif x < 0 and y < 0:
        coord['Q3'] = coord.get('Q3', 0) + 1
    elif x > 0 and y < 0:
        coord['Q4'] = coord.get('Q4', 0) + 1
    else:
        coord['AXIS'] = coord.get('AXIS', 0) + 1
for k, v in coord.items():
    print(f'{k}: {v}')  
