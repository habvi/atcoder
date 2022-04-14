n, K = map(int, input().split())
A = list(map(int, input().split()))

mx = len(bin(K)) - 2

zero = False
x = K
for i in reversed(range(mx)):
    one = 0
    for a in A:
        one += a >> i & 1

    if one > n // 2 and K >> i & 1:
        x ^= 1 << i
        zero = True
        continue

    if (one <= n // 2) and (not K >> i & 1) and zero:
        x |= 1 << i

print(sum(x ^ a for a in A))