n, K = map(int, input().split())
A = list(map(int, input().split()))

if n == K:
    print(1)
    exit()

n -= K
w = K - 1
ans = (n + w - 1)//w + 1
print(ans)