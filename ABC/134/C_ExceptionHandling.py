n = int(input())
A = [int(input()) for _ in range(n)]
sa = sorted(A)
mx = sa[-1]
second = sa[-2]

for a in A:
    if a == mx:
        ans = second
    else:
        ans = mx
    print(ans)