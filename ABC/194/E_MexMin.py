from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))

count_ = Counter(A[:m])

now = 0
while count_[now]:
    now += 1

for i in range(m, n):
    a = A[i]
    count_[a] += 1

    rm = A[i - m]
    count_[rm] -= 1
    if count_[rm] == 0:
        now = min(now, rm)

print(now)