n, K = map(int, input().split())
A = list(map(int, input().split()))

mx = 40
x = 0
for i in reversed(range(mx)):
    zero, one = 0, 0
    for a in A:
        if a >> i & 1:
            one += 1
        else:
            zero += 1

    if one < zero:
        x |= 1 << i

    if x > K:
        x ^= 1 << i

print(sum(x ^ a for a in A))