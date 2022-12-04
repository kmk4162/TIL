import sys
input = sys.stdin.readline

tree, target = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
# 시작은 중간값
start = 0
end = trees[-1] # 테케2 기준 42
# print(standard_height)
answer = 0
while start <= end:
    tree_total = 0
    standard_height = (start + end) // 2
    for tree in trees:
        if tree > standard_height: 
            tree_total += (tree - standard_height)
    if tree_total >= target:
        answer = standard_height
        start = standard_height + 1
    else:
        end = standard_height - 1
print(answer)