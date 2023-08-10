N = int(input())
A = list(map(int, input().split()))

total = sum(A)
div, mod = divmod(total, N)
target = [div] * (N - mod) + [div + 1] * mod
A.sort()

ans = 0
for a, t in zip(A, target):
    if t > a:
        ans += (t - a)
print(ans)