n = int(input())

n += 1
k = len(str(n))
mod = 10
ans = 0
for i in range(k):
    ans += (n // mod) * (mod // 10)
    ans += min(max(0, n % mod - mod //10), mod // 10)
    mod *= 10
print(ans)