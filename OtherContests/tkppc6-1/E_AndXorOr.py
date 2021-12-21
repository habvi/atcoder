n = int(input())
A = list(map(int, input().split()))

m = len(bin(max(A))) - 2
k = 1 << m - 1
ans = 0
for _ in range(m):
    nxt = []
    for a in A:
        if a & k:
            nxt.append(a)

    if len(nxt) >= 2:
        A = nxt
        ans |= k
    k >>= 1
print(ans * 2)