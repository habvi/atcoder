w, h = map(int, input().split())
if w % 16 == h % 9 == 0:
    print('16:9')
else:
    print('4:3')



# w, h = map(int, input().split())
# if w * 3 == h * 4:
#     print('4:3')
# else:
#     print('16:9')