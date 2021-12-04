n = int(input())
p = [int(input()) for _ in range(n)]
cnt = [0] * (n + 1)
for i in range(n):
    cnt[p[i]] += max(1, cnt[p[i] - 1] + 1)
print(n - max(cnt))