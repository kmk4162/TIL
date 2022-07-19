default = ['+', '+', '+', '+', '+']
for i in range(5):
    default.insert(i,'#')
    default.pop()
    print(''.join(default))
    default = ['+', '+', '+', '+', '+']