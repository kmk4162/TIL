word = input()
my_dict = {}

for i in range(len(word)):
    my_dict[word[i]] = my_dict.get(word[i], 0) + 1

for i in my_dict:
    print(f'{i} {my_dict[i]}')