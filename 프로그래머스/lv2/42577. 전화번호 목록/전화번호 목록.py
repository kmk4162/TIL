def solution(phone_book):
    phone_dict = {}
    for phone_number in phone_book:
        phone_dict[phone_number] = 1
    
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in phone_dict and jubdoo != phone_number:
                return False
    return True
