N, A, B = map(int, input().split())

if N < A:
    print(0)
    exit()

cand = N - (A - 1)
if A <= B:
    print(cand)
    exit()

ans = B * (cand // A)
ans += min(B, cand % A)
print(ans)