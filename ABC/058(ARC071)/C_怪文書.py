from collections import Counter
n = int(input())
a = Counter(input())
for _ in range(n - 1):
    a &= Counter(input())

ans = ""
for k, v in a.items():
    ans += k * v
print("".join(sorted(ans)))