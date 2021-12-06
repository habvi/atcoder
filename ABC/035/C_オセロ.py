from itertools import accumulate
n, q = map(int, input().split())
cnt = [0] * (n + 1)
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    cnt[l] += 1
    cnt[r] -= 1
    
ac = list(accumulate(cnt))
ans = ''
for a in ac[:-1]:
    if int(a) % 2 == 0:
        ans += '0'
    else:
        ans += '1'
print(ans)