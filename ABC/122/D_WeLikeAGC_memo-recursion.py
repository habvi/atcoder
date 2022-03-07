from collections import defaultdict

def ok(S):
    ng = 'AGC'
    if ng in S:
        return False

    for i in range(3):
        T = list(S)
        T[i], T[i + 1] = T[i + 1], T[i]
        if ng in ''.join(T):
            return False
    return True


def dfs(i, S):
    if memo[i][S]:
        return memo[i][S]
    if i == n:
        return 1

    res = 0
    for c in 'ACGT':
        if ok(S + c):
            res += dfs(i + 1, S[1:] + c)
            res %= MOD
    memo[i][S] = res
    return res


n = int(input())
MOD = 10**9 + 7

memo = [defaultdict(int) for _ in range(n + 1)]

print(dfs(0, 'XXX'))