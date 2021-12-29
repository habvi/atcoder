s = [input() for _ in range(12)]
ans = 0
for t in s:
    if 'r' in t:
        ans += 1
print(ans)