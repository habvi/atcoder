N = int(input())

one = 0
k = N.bit_length()
for i in range(k):
    one += (N >> i & 1)

for bit in range(1 << one):
    ans = 0
    j = 0
    for i in range(k):
        if N >> i & 1:
            if bit >> j & 1:
                ans |= 1 << i
            j += 1
    print(ans)