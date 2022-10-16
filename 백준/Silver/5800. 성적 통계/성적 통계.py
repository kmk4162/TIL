T = int(input())

for testcase in range(T):
    A = list(map(int, input().split()))
    students = A[1:]
    high = max(students)
    low = min(students)

    # 정렬 후 인접 점수 차이 구하기
    largest_gap = 0
    students.sort(reverse = True)
    for i in range(1, A[0]):
        gap = students[i-1] - students[i]
        if gap > largest_gap:
            largest_gap = gap
    print(f'Class {testcase + 1}')
    print(f'Max {high}, Min {low}, Largest gap {largest_gap}')