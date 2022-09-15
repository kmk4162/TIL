div_list = []
for i in range(10):
    number = int(input())
    div = number % 42
    div_list.append(div)
print(len(set(div_list)))

