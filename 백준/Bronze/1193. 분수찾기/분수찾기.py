X = int(input())
range_ = 1
before_range_ = 0
# 분모 분자 합
sum_ = 2
while True:
    if X <= range_:
        # cur은 대각선 인덱스 표현
        cur = X - before_range_
        if sum_ % 2 == 1:
            top = cur
            bottom = sum_ - top
            break
        else:
            bottom = cur
            top = sum_ - bottom
            break
    else:
        before_range_ = range_
        range_ += sum_
        sum_ += 1
print(top,'/',bottom, sep = '')