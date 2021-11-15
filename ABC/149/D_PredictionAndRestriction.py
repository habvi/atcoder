from itertools import groupby
n, K = map(int, input().split())
r, s, p = map(int, input().split())
T = input()
jan = 'rsp'
win = [p, r, s]
ans = 0
for i in range(K):
    a = [T[j] for j in range(i, n, K)]
    for k, g in groupby(a):
        ans += win[jan.index(k)] * ((len(list(g)) + 1) // 2)
print(ans)



'''
前回貪欲法
'''
n, k = map(int, input().split())
r, s, p = map(int, input().split())
rsp = [r, s, p]
T = input()
S = ''
a = [True]*n

for t in T:
    if t == 'r':
        S += '2'
    elif t == 's':
        S += '0'
    else:
        S += '1'

ans = 0
for i in range(n):
    if not a[i]:
        continue
    if i < n-k:
        if S[i] == S[i+k]:
            a[i+k] = False
    ans += rsp[int(S[i])]
print(ans)