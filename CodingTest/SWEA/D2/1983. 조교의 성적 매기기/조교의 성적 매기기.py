T = int(input())
grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(T):
    # N은 학생 수, K는 학점 알고싶은 학생의 번호
    N, K = map(int, input().split())

    # 학생들을 순서대로 리스트에 넣기 + N개 입력 만큼 자리수 설정해두기
    student_list = [0 for i in range(N)]
    for i in range(N):
        mid, final, assign = map(int, input().split())
        student_list[i] = mid * 0.35 + final * 0.45 + assign * 0.2
    
    # K가 3이라면 인덱스가 2이기때문에 -1처리
    k_score = student_list[K - 1]

    # 내림차순 정렬
    student_list.sort(reverse = True)

    # K번째 학생의 점수를 알고있고, 새로 정렬한 리스트에서 해당하는 점수의
    # 인덱스(등수)를 찾는 과정
    k_rank = student_list.index(k_score)

    # N명에 따른 성적 구간 나누기
    # 항상 10단위로 나뉘니까 N이 몇명이 들어오든 10으로 나눠서 계산
    R = N // 10 
    grade = k_rank // R
    print(f'#{test_case + 1}', grade_list[grade])