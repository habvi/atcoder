def ceil(a, b):
    return (a + b - 1) // b


N, K = map(int, input().split())
A = list(map(int, input().split()))

x = 0
bit = (10 ** 12).bit_length()
for b in reversed(range(bit)):
    zero = 0
    for a in A:
        zero += not (a >> b & 1)

    if zero >= ceil(N, 2) and (x | 1 << b) <= K:
        x |= 1 << b

print(sum(a ^ x for a in A))