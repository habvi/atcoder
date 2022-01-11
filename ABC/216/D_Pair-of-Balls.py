from collections import deque, defaultdict
n, m = map(int, input().split())
q = deque([])
cnt = defaultdict(int)
A = []
for i in range(m):
    k = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    ba = a.pop()
    if ba in cnt:
        q.append(cnt[ba])
        q.append(i)
    else:
        cnt[ba] = i
    A.append(a)

tot = 0
while q:
    x = q.popleft()
    y = q.popleft()
    for i in (x, y):
        if A[i]:
            ba = A[i].pop()
            if ba in cnt:
                q.append(cnt[ba])
                q.append(i)
            else:
                cnt[ba] = i
    tot += 1
print('Yes' if tot == n else 'No')