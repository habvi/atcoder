n = int(input())
A = list(map(int, input().split()))

ans = float('inf')
for cut in range(1 << n):
    xor = 0
    or_ = 0
    for i, a in enumerate(A):
        or_ |= a
        if cut >> i & 1:
            xor ^= or_
            or_ = 0
    xor ^= or_
    ans = min(ans, xor)
print(ans)