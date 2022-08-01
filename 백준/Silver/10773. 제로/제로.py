T = int(input())
num_list = []

for i in range(T):
    number = int(input())
    if number == 0:
        num_list.pop()
    else:
        num_list.append(number)
print(sum(num_list))