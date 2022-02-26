n = int(input())
A = []
for _ in range(n):
    a = int(input())
    A.append([tuple(map(int, input().split())) for _ in range(a)])

ans = 0
for bit in range(1 << n):
    honest = 0
    for i, a in enumerate(A):
        if bit >> i & 1:
            for pi, say in a:
                pi -= 1
                if bit >> pi & 1 != say:
                    break
            else:
                honest += 1
    if honest == bin(bit).count('1'):
        ans = max(ans, honest)

print(ans)