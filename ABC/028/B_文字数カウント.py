S = input()
ans = [0] * 6
for s in S:
    ans[ord(s) - ord('A')] += 1
print(*ans)