N = int(input())

one = []
k = N.bit_length()
for i in range(k):
    if N >> i & 1:
        one.append(i)

for bit in range(1 << len(one)):
    ans = 0
    j = 0
    for i in range(k):
        if N >> i & 1:
            if bit >> j & 1:
                ans |= 1 << i
            j += 1
    print(ans)