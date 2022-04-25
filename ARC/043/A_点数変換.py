n, A, B = map(int, input().split())
S = [int(input()) for _ in range(n)]

S.sort()
mn, mx = S[0], S[-1]
total = sum(S)

if mx == mn:
    print(-1)
    exit()

P = B / (mx - mn)
print(P, A - total * P / n)