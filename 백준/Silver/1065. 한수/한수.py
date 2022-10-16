num= int(input())
hansu = []
cnt = 0
#* 1. 1부터 99까지는 전부 한수, 100이상부터 따로 생각하기
for number in range(1, 100):
    hansu.append(number)

#* 2. 등차가 0인 한수들 리스트에 추가
def same_difference():
    for i in range(1, 10):
        number = (100 * i + 10 * i + i)
        hansu.append(number)
        
#* 3. 등차가 양수인 한수들 리스트에 추가
def increase_difference():
    for deungcha in range(1, 5): # 최대 등차가 4임(159나 951같이)
        baek = 1 
        while baek + (2 * deungcha) < 10:
            number = (100 * baek  + 10 * (baek + deungcha) + baek + (deungcha * 2))
            baek += 1
            hansu.append(number)

#* 4. 등차가 음수인 한수들 리스트에 추가            
def decrease_difference():
    for deungcha in range(-4, 0): 
        baek = 9 # baek은 백의자리
        while baek + (2 * deungcha) >= 0:
            number = (100 * baek  + 10 * (baek + deungcha) + baek + (deungcha * 2))
            baek -= 1
            hansu.append(number)

#* 5 한수들 전부 리스트에 넣고 정렬한 다음에 인풋보다 작은 수까지의 한수들 구하기
same_difference()
increase_difference()
decrease_difference()

for i in sorted(hansu):
    if i <= num:
        cnt += 1
    else: break
print(cnt)
