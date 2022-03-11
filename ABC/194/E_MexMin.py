from collections import defaultdict

n, m = map(int, input().split())
A = list(map(int, input().split()))

count_ = defaultdict(int)
for i in range(m):
    a = A[i]
    count_[a] += 1

for i in range(n):
    if count_[i] == 0:
        now = i
        break
else:
    now = max(A) + 1

for i in range(m, n):
    a = A[i]
    count_[a] += 1

    rm = A[i - m]
    count_[rm] -= 1
    if count_[rm] == 0 and rm < now:
        now = rm
print(now)