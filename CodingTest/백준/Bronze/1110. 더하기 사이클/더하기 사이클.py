N = int(input())

cnt = 0
new_number = N

while True:
    cnt += 1
    tens = new_number // 10
    units = new_number % 10
    new_number = tens + units # 각 자리수 덧셈해서 새로운 숫자 생성
    new_number_units = new_number % 10 
    final_number = units * 10 + new_number_units
    # 이전 단계의 일의 자리 숫자를 십의자리로 하고,
    # new_number의 일의 자리 숫자를 일의자리로 쓰는 숫자로 업데이트!
    if N == final_number:
        print(cnt)
        break
    else:
        new_number = final_number

