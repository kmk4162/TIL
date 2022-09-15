while True:
    allbigcnt = 0
    allcnt = 0
    list_ = []
    line = input()
    if line == '.':
        break
    for char in line:
        if char == '[':
            list_.append(char)
        elif char == '(':
            list_.append(char)
        elif char == ']':
            if len(list_) == 0:
                list_.append(char)
            else:
                if list_[-1] == '[':
                    list_.pop()
                else:
                    list_.append(char)        
        elif char == ')':
            if len(list_) == 0:
                list_.append(char)
            else:
                if list_[-1] == '(':
                    list_.pop()
                else:
                    list_.append(char)
    if len(list_) == 0:
        print('yes')
    else:
        print('no')
