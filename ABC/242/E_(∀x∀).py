def stoi(s):
    return ord(s) - ord('A')

def count_palindrome(S):
    T = S[:mid + 1][::-1] if n % 2 else S[:mid][::-1]
    total = 1
    k = 1
    for t in T:
        total += k * stoi(t)
        total %= MOD
        k *= 26
        k %= MOD

    return total


T = int(input())
MOD = 998244353

for _ in range(T):
    n = int(input())
    S = list(input())

    mid = n // 2
    half = S[:mid]
    T = half[:]
    if n % 2:
        T.append(S[mid])
    T.extend(half[::-1])

    ans = count_palindrome(T)
    if T > S:
        ans -= 1
    print((ans + MOD) % MOD)