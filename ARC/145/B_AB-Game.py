N, A, B = map(int, input().split())

if N < A:
    print(0)
    exit()

ans = N - (A - 1)
if A <= B:
    print(ans)
    exit()

block = (N - (A - 1)) // A
ans = B * block
ans += min(B, (N - (A - 1)) % A)
print(ans)