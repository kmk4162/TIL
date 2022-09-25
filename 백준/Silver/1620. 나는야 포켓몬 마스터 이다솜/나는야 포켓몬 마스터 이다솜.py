import sys
input = sys.stdin.readline

# M개 입력 받고, N번 요청에 응답하기
M, N = map(int, input().split())

pokemon = {}
for idx in range(1, M + 1):
    name = input().rstrip()
    pokemon[name] = idx
    pokemon[str(idx)] = name

for _ in range(N):
    cmd = input().rstrip()
    print(pokemon[cmd])