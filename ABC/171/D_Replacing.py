from collections import Counter
n = int(input())
a = list(map(int, input().split()))
q = int(input())
cnt = Counter(a)
    
tot = sum(a)
for _ in range(q):
    b, c = map(int, input().split())
    tot += (c - b) * cnt[b]
    cnt[c] += cnt[b]
    cnt[b] = 0
    print(tot)