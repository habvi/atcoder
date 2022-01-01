a, b, c, d = map(int, input().split())
while True:
    if c <= 0:
        print('Yes')
        exit()
    if a <= 0:
        print('No')
        exit()
    c -= b
    a -= d



# a, b, c, d = map(int, input().split())
# x = (a + d - 1)//d
# y = (c + b - 1)//b
# print('Yes' if x >= y else 'No')