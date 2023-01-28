S = input()
T = input()

n = len(S)
m = len(T)
is_same = [0] * (n + 2)
is_same[0] = 1
is_same[n + 1] = 1
for i, t in enumerate(T[::-1]):
    s = S[n - i - 1]
    is_same[n - i] = (t == s or t == '?' or s == '?') & is_same[n - i + 1]

for l in range(m + 1):
    t = T[l - 1]
    s = S[l - 1]
    if l >= 1:
        is_same[l] = (t == s or t == '?' or s == '?') & is_same[l - 1]
    r = n - m + l + 1
    if is_same[l] and is_same[r]:
        print("Yes")
    else:
        print("No")


'''
abc?efgb?c
      abzc
a      bzc
ab      zc
abz      c
abzc

abc?efgb?c
abzc
'''