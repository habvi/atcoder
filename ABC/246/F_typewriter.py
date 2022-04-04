def stoi(s):
    return ord(s) - ord('a')


n, L = map(int, input().split())
MOD = 998244353

alph = [0] * n
for i in range(n):
    S = input()
    for s in S:
        alph[i] |= (1 << stoi(s))

ans = 0
for bit in range(1, 1 << n):
    is_odd = bin(bit).count('1')

    common = (1 << 26) - 1
    for i in range(n):
        if bit >> i & 1:
            common &= alph[i]

    num = bin(common).count('1')
    ans += pow(num, L, MOD) * (1 if is_odd % 2 else -1)
    ans %= MOD

print(ans)