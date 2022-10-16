chess = [1, 1, 2, 2, 2, 8]

chessinput = list(map(int, input().split()))

for i in range(len(chessinput)):
    result = chess[i] - chessinput[i]
    print(result, end = ' ')
