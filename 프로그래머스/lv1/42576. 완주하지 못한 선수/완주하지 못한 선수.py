def solution(participant, completion):
    dict_ = {}
    for i in participant:
        dict_[i] = dict_.get(i, 0) + 1
    for j in completion:
        dict_[j] -=1
    for k in dict_:
        if dict_[k] == 1:
            return k