from collections import Counter, deque

n, m = map(int, input().split())
A = list(map(int, input().split()))

count_ = Counter()
q = deque([])
for a in A[:m]:
    count_[a] += 1
    q.append(a)

now = 0
while count_[now]:
    now += 1

for a in A[m:]:
    count_[a] += 1
    q.append(a)

    rm = q.popleft()
    count_[rm] -= 1
    if count_[rm] == 0:
        now = min(now, rm)

print(now)