N = int(input())
result = 1
gen_list = []
while result < N:
    digits = 0
    generator = 0
    for i in str(result):
        digits += int(i)
    generator = result + digits

    if generator == N:
        print(result)
        gen_list.append(result)
        break
    else:
        result += 1
        continue
if bool(gen_list) == False:
    print(0)
