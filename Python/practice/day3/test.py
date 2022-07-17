def toki(**tokens):
    print(tokens)

my_dict = {
    'name' : 'kevin',
    'age' : '25',
    'height' : '175'
}
toki(**my_dict)


# toki(a=1, b=2, c=3, d=4)