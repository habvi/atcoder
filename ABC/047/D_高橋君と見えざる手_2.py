from collections import defaultdict
n, t = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
mn = float('inf')
mx_diff = 0
ans = defaultdict(int)
for a in A:
    cnt[a] += 1
    if a <= mn:
        mn = a
        continue
    diff = a - mn
    if mx_diff > diff:
        continue
    elif mx_diff < diff:
        ans = defaultdict(int)
        
    mx_diff = diff
    ans[(mn, a)] = min(cnt[mn], cnt[a])
    
print(sum(ans.values()))


'''
5 2
5 5 7 7 7

5 2
5 5 5 7 7

9 4
5 5 5 7 7 5 5 5 5

10 100
7 10 4 5 9 3 6 8 2 1

5 5
4 9 4 4 9

9 5
4 5 9 4 9 5 4 9 9
'''