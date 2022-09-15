while True:
    cnt_small = 0
    cnt_big = 0
    cnt_num = 0
    cnt_space = 0
    try:
        line = input()    
        for char in line:
            if 65 <= ord(char) <= 90:
                cnt_big += 1
            elif 97 <= ord(char) <= 122:
                cnt_small += 1
            elif 48 <= ord(char) <= 57:
                cnt_num += 1
            elif char == ' ':
                cnt_space += 1
        print(cnt_small, cnt_big, cnt_num, cnt_space) 
        continue
    except:
        break