s = input()
t = input()
ans = set()
for a, b in zip(s, t):
    ans.add((ord(a) - ord(b)) % 26)
print('Yes' if len(ans) == 1 else 'No')