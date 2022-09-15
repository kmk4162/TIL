words = input()

happy = words.count(':-)')
sad = words.count(':-(')

if happy == sad:
    if happy == 0 and sad == 0:
        print('none')
    else:
        print('unsure')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')