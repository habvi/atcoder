import statistics

def sigma(n):
    return n*(n + 1) // 2


N = int(input())
S = input()

one_idx = [i for i, s in enumerate(S) if s == '1']
median = int(statistics.median(one_idx))
left, right = 0, 0
ans = 0
for i, s in enumerate(S):
    if s == '0':
        continue
    if i < median:
        left += 1
    elif median < i:
        right += 1
    ans += abs(i - median)
if S[median] == '0':
    left -= 1

print(ans - sigma(left) - sigma(right))
