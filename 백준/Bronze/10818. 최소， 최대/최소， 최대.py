N = int(input())

list1 = list(map(int, input().split()))
big = list1[0]
small = list1[0]

for number in list1:
    if number >= big:
        big = number
    elif number < small:
        small = number
print(small, big)