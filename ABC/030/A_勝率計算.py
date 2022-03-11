a, b, c, d = map(int, input().split())

T = b / a
A = d / c

if T > A:
    print('TAKAHASHI')
elif T < A:
    print('AOKI')
else:
    print('DRAW')