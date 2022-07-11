a, b, c = map(int, input().split())

sum1 = sum((a, b, c))
avg1 = sum1 / 3
avg1_final = format((avg1), '.2f')

print(sum1, avg1_final, sep = ' ')