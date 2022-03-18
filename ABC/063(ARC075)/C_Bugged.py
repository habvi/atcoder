n = int(input())

mn = float('inf')
total = 0
for _ in range(n):
    s = int(input())
    total += s
    if s % 10:
        mn = min(mn, s)

if mn == float('inf'):
    ans = 0
else:
    ans = total if total % 10 else total - mn
print(ans)