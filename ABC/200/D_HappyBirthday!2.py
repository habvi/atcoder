n = int(input())
A = list(map(int, input().split()))
MOD = 200

# 2**8 - 1 = 255 > 200
n = min(n, 8)
A = [a % MOD for a in A[:n]]

for b in range(1, 1 << n):
    for c in range(1, 1 << n):
        if b == c:
            continue

        B = []
        sumb = 0
        for i in range(n):
            if b >> i & 1:
                B.append(i + 1)
                sumb += A[i]
                sumb %= MOD

        C = []
        sumc = 0
        for i in range(n):
            if c >> i & 1:
                C.append(i + 1)
                sumc += A[i]
                sumc %= MOD

        if sumb == sumc:
            print('Yes')
            print(len(B), *B)
            print(len(C), *C)
            exit()

print('No')
