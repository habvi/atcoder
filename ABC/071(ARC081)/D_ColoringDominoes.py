n = int(input())
S1 = input()
S2 = input()
MOD = 10**9 + 7

if S1[0] == S2[0]:
    ans = 3
    pattern = 0
    i = 1
else:
    ans = 6
    pattern = 1
    i = 2

while i < n:
    if pattern:
        if S1[i] == S2[i]:
            pattern = 0
            i += 1
        else:
            ans *= 3
            i += 2
    else:
        ans *= 2
        if S1[i] == S2[i]:
            i += 1
        else:
            pattern = 1
            i += 2
    ans %= MOD
print(ans)