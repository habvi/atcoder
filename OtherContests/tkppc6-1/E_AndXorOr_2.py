n = int(input())
A = list(map(int, input().split()))

k = len(bin(max(A))) - 2
for i in range(k - 1, -1, -1):
    nxt = []
    for a in A:
        if a&(1 << i):
            nxt.append(a)

    if len(nxt) >= 2:
        A = nxt

a, b = A[:2]
print(a + b - ((a&b) ^ (a|b)))