a, b = map(int, input().split())

if a == 1:
    if b in (2, 10):
        print('Yes')
    else:
        print('No')
else:
    if a + 1 == b:
        print('Yes')
    else:
        print('No')