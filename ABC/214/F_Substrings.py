def right_leftmost_idx(S):
    def stoi(s):
        return ord(s) - ord('a')

    n = len(S)
    idx = [[n] * 26 for _ in range(n + 1)]
    for i in reversed(range(n)):
        for alph in range(26):
            if stoi(S[i]) == alph:
                idx[i][alph] = i
            else:
                idx[i][alph] = idx[i + 1][alph]
    return idx


S = input()
n = len(S)
MOD = 10**9 + 7

idx = right_leftmost_idx(S)
dp = [0] * (n + 2)
dp[0] = 1

for i in range(n + 1):
    for j in range(26):
        nxt = idx[i][j]
        if nxt >= n:
            continue

        dp[nxt + 2] += dp[i]
        dp[nxt + 2] %= MOD

print((sum(dp) - 1) % MOD)