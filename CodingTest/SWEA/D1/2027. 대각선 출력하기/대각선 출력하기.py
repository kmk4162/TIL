# 주어진 텍스트를 그대로 출력하세요.

# 출력
'''
#++++
+#+++
++#++
+++#+
++++#
'''

#* ------------------------------------------------------------------------------------
#* case1
# print('#++++')
# print('+#+++')
# print('++#++')
# print('+++#+')
# print('++++#')

#* case2
# default = ['+', '+', '+', '+', '+']
# for i in range(5):
#     default.insert(i,'#')
#     default.pop()
#     print(''.join(default))
#     default = ['+', '+', '+', '+', '+']

#* case3 리스트화
# default = ['+', '+', '+', '+', '+']
# default_list = list(default)
# for i in range(len(default_list)):
#     default_list[i] = '#'
#     print(''.join(default_list))
#     default = ['+', '+', '+', '+', '+']
#     default_list = list(default)

#* case4 반복문 2번
#* 좌표 평면처럼 생각하자. (0,1), (3,4) 처럼!
#? print함수 안에 아무것도 안 넣고 그냥 print()만 하면 줄바꿈!
for x in range(5):
    for y in range(5):
        if x == y: print('#', end = '')
        else: print('+', end = '')
    print()
