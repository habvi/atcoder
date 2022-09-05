from itertools import accumulate

N = int(input())
S = input()

R = [(s == 'R') * 1 for s in S]
G = [(s == 'G') * 1 for s in S]
B = [(s == 'B') * 1 for s in S]
ac = [list(accumulate(R)), list(accumulate(G)), list(accumulate(B))]
rgb = "RGB"
ans = 0
for l in range(N):
    for m in range(l + 1, N):
        if S[l] == S[m]:
            continue
        si = rgb.index(S[l])
        sj = rgb.index(S[m])
        k = 3 - si - sj
        s = rgb[k]
        ans += (ac[k][-1] - ac[k][m])
        r = 2 * m - l
        if r < N and S[r] == s:
            ans -= 1
print(ans)