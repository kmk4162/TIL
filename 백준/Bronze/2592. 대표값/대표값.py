dict_ = {}
for i in range(10):
    num = int(input())
    dict_[num] = dict_.get(num, 0) + 1

cnt = 0
for i, j in dict_.items():
    cnt += i * j
avg = cnt / 10
dict_ = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
print(int(avg))
print(dict_[0][0])

