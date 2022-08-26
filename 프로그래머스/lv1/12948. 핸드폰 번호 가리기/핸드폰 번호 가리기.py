def solution(phone_number):
    l = len(phone_number)
    forward_ = '*' * (l - 4)
    backward_ = phone_number[l-4:]
    return forward_ + backward_