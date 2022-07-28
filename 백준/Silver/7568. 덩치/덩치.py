N = int(input())
spec_list = []
ranks = [0] * N

for i in range(N):
    spec = list(map(int, input().split()))
    spec_list.append(spec)

for a in range(len(spec_list)):
    # A = spec_list[a] 이라고 여기 쓰고 쭉 이용할 수 있음
    # 코드가 더욱 간단해짐
    for b in range(len(spec_list)):
        # B = spec_list[b] 로 쓰면 더욱 간단,
        # spec_list[b][0] 대신 B[0] 이렇게 가능!
        #! b가 확실하게 a보다 덩치가 작다
        #! 그러니 b보다 덩치가 큰 사람이 한명 더 있다
        if spec_list[a][0] > spec_list[b][0] and spec_list[a][1] > spec_list[b][1]:
            ranks[b] += 1
        # print(spec_list[a][0], spec_list[a][1])
        # print(spec_list[b][0], spec_list[b][1])
        # print(ranks)
for i in ranks:
    i += 1
    print(i, end = ' ')