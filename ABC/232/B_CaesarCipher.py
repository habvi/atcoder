S = input()
T = input()

ans = set()
for s, t in zip(S, T):
    ans.add((ord(s) - ord(t)) % 26)
print("Yes" if len(ans) == 1 else "No")