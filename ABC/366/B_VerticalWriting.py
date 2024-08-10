N = int(input())

S = [input() for _ in range(N)]

max_len = 0
for s in S:
    max_len = max(max_len, len(s))

ans = [["*"] * N for _ in range(max_len)]
for i, s in zip(range(N - 1, -1, -1), S):
    for j in range(len(s)):
        ans[j][i] = s[j]

for a in ans:
    print("".join(a).rstrip("*"))
