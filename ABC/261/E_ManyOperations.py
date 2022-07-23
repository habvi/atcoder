N, C = map(int, input().split())

X = C
zero = 0
one = (1 << 30) - 1
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

    ans = 0
    for i in range(30):
        if X >> i & 1:
            bit = one >> i & 1
            if bit:
                ans |= 1 << i
        else:
            bit = zero >> i & 1
            if bit:
                ans |= 1 << i
    print(ans)
    X = ans