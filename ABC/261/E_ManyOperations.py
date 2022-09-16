N, C = map(int, input().split())

zero = 0
one = ~0
x = C
for _ in range(N):
    t, a = map(int, input().split())
    if t == 1:
        zero &= a
        one &= a
    elif t == 2:
        zero |= a
        one |= a
    else:
        zero ^= a
        one ^= a
    x = (x & one) | (~x & zero)
    print(x)