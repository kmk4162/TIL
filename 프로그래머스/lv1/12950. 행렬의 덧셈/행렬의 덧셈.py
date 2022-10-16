def solution(arr1, arr2):
    x = len(arr1[0])
    for i in range(len(arr1)):
        for j in range(x):
            arr1[i][j] += arr2[i][j]
    return arr1